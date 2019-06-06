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

    def apply(self, word: str) -> List[str]:
        results = self.compute_tree(self.tree, [word])
        return results


class WholeRule:
    def __init__(self, name: str, pos_b: str, pos_a: str, info: str = '', subrules: List[SubRule] = None):    
        self.name = name
        self.info = info
        self.pos_a = pos_a
        self.pos_b = pos_b
        self.subrules = subrules if subrules is not None else []

    def apply(self, word: str):
        results = []
        for subrule in self.subrules:
            results.extend(subrule.apply(word))
        return results


def load_rules_from_json(json_file, tag_type='b'):
    rules = []
    with open(json_file, encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
        for json_rule in data['data']:
            subrules = list()
            for case in json_rule['cases']:
                subrules.append(SubRule(tags_b=case[f'tags_{tag_type}'], raw_rules=case['rules']))
            rules.append(WholeRule(
                name=json_rule.get('rule_id'), 
                pos_b=json_rule.get('pos_b'), 
                pos_a=json_rule.get('pos_a'), 
                info=json_rule.get('info'),
                subrules=subrules))
    return rules
