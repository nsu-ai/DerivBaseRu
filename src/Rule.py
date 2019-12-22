import json
from lark.tree import pydot__tree_to_png

from src.loading_rules_to_tree import *
from src.functions import *


class SubRule:
    def __init__(self, tags_b: Dict[str, str], raw_rules: str):
        self.tags_b = dict()
        for tag in tags_b:
            possible_values = tags_b[tag].split(',')
            self.tags_b[tag] = possible_values
        self.logical_form, self.operators = normalize_raw_text(raw_rules)
        self.tree = short_parser.parse(self.logical_form)

    def plot_tree(self, filename: str='tree'):
        pydot__tree_to_png(self.tree, filename + ".png")

    def compute_tree(self, tree, cur_results: List[str]) -> List[str]:
        if hasattr(tree.children[0], 'value'):
            command = self.operators[int(tree.children[0].value)]
            new_results = []
            for word in cur_results:
                new_results += eval(command)
        elif tree.children[0].data == 'or':
            new_results = []
            for child in tree.children[0].children:
                new_results += self.compute_tree(child, cur_results)
        elif tree.children[0].data == 'and':
            new_results = self.compute_tree(tree.children[0].children[0], cur_results)
            new_results = self.compute_tree(tree.children[0].children[1], new_results)
        else:
            new_results = []
        return new_results

    def check(self, **kwargs) -> bool:
        for tag in self.tags_b:
            if kwargs.get(tag) is not None and not (set(kwargs[tag]) & set(self.tags_b[tag])):
                return False
        return True

    def apply(self, word_b: str, **kwargs) -> List[str]:
        if not self.check(**kwargs):
            return []
        results = self.compute_tree(self.tree, [word_b])
        return results


class WholeRule:
    def __init__(self, name: str, pos_b: str, pos_a: str, info: str = '', only_complex: bool = False, rare: List[str] = [], subrules: List[SubRule] = None):
        self.name = name
        self.info = info
        self.pos_a = pos_a
        self.pos_b = pos_b
        self.only_complex = only_complex
        self.rare = list(map(lambda x: x.split(';'), rare))
        self.subrules = subrules if subrules is not None else []

    def __repr__(self):
        return self.name

    def check(self, pos_b: str = None, pos_a: str = None):
        return self.pos_b == pos_b and self.pos_a == pos_a

    def apply(self, word_b: str, **kwargs):
        results = []
        for subrule in self.subrules:
            results.extend(subrule.apply(word_b, **kwargs))
        return results

    def apply_with_tags(self, word_b: str, pos_b: str = None, pos_a: str = None, **kwargs):
        if not self.check(pos_b, pos_a):
            return []
        return self.apply(word_b, **kwargs)


class ComplexRule(WholeRule):
    def __init__(self, name: str, pos_b: str, pos_a: str, info: str = '', only_complex: bool = False, rare: List[str] = [], simple_rule_ids: List[str] = None):
        WholeRule.__init__(self, name, pos_b, pos_a, info, only_complex, rare, None)
        self.simple_rule_ids = simple_rule_ids if simple_rule_ids is not None else []
        self.simple_rules = []  # need to get WholeRule_s by their ids later in Derivation class

    def apply(self, word: str, **kwargs):
        cur_results = [word]
        for simple_rule in self.simple_rules:
            new_results = []
            for word in cur_results:
                new_results.extend(simple_rule.apply(word))
            cur_results = new_results
        return cur_results

    def apply_with_tags(self, word_b: str, pos_b: str = None, pos_a: str = None, **kwargs):
        if not self.check(pos_b, pos_a):
            return []
        # TODO: make possible inner tag analysis by Guesser
        cur_results = [word_b]
        for simple_rule in self.simple_rules:
            new_results = []
            for word in cur_results:
                new_results.extend(simple_rule.apply(word, **kwargs))
            #kwargs = dict()
            cur_results = new_results
        return cur_results


def load_rules_from_json(json_file, tag_type='b'):
    rules = []
    with open(json_file, encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
        for json_rule in data['data']:
            try:
                subrules = list()
                if json_rule.get('cases') is not None:
                    for i, case in enumerate(json_rule['cases']):
                        subrules.append(SubRule(tags_b=case[f'tags_{tag_type}'], raw_rules=case['rules']))
                    rules.append(WholeRule(
                        name=json_rule.get('rule_id'),
                        pos_b=json_rule.get('pos_b'),
                        pos_a=json_rule.get('pos_a'),
                        info=json_rule.get('info'),
                        only_complex=json_rule.get('only_complex') is not None,
                        rare=json_rule.get('rare') if json_rule.get('rare') is not None else [],
                        subrules=subrules))
                else:
                    for rule_id in json_rule['complex']:
                        subrules.append(rule_id)
                    rules.append(ComplexRule(
                        name=json_rule.get('rule_id'),
                        pos_b=json_rule.get('pos_b'),
                        pos_a=json_rule.get('pos_a'),
                        info=json_rule.get('info'),
                        only_complex=False,#json_rule.get('only_complex') is not None,
                        rare=json_rule.get('rare') if json_rule.get('rare') is not None else [],
                        simple_rule_ids=subrules))
            except:
                print("ERROR reading a rule!", json_rule.get('rule_id'))

    return rules
