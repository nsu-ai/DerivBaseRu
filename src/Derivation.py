import os

from src.guesser.ZaliznyakGuesser import *


class Derivation:
    def __init__(self):
        # self.tag_guesser = ZaliznyakGuesser()
        self.rules = list()
        for pos in {'adv', 'adj'}:
            derivation_rules = os.path.join(os.path.dirname(__file__), 'rules', 'rules_{}.json'.format(pos))
            if not os.path.isfile(derivation_rules):
                continue
            with open(derivation_rules, encoding='utf-8') as data_file:
                data = json.loads(data_file.read())
            for json_rule in data['data']:
                new_rule = list()
                rule_id = json_rule['rule_id']
                pos_b = json_rule['pos_b']
                pos_a = json_rule['pos_a']
                for case in json_rule['cases']:
                    name = rule_id + ':' + case['case_id']
                    tags_b = case['tags_b']
                    raw_rules = case['rules']
                    new_case = Rule(name=name, pos_b=pos_b, pos_a=pos_a, tags_b=tags_b, raw_rules=raw_rules)
                    new_rule.append(new_case)
                self.rules.extend(new_rule)

    # def derive_with_pos(self, word_b: str, pos_b: str, pos_a: str, rule_id: str=None) -> List[Tuple[str, str]]:
    def derive_with_pos(self, word_b: str, pos_b: str, pos_a: str, rule_id: str=None) -> List[str]:
        results = list()
        if not rule_id:
            for rule in self.rules:
                if rule.tags_b['pos_b'] == pos_b and rule.pos_a == pos_a:
                    new_results = rule.apply(word_b)
                    for word_result in new_results:
                        # result = (word_result, rule.name)
                        results.append(word_result)
        else:
            for rule in self.rules:
                if rule.name != rule_id:
                    continue
                if rule.tags_b['pos_b'] == pos_b and rule.pos_a == pos_a:
                    new_results = rule.apply(word_b)
                    for word_result in new_results:
                        # result = (word_result, rule.name)
                        results.append(word_result)
        return results

    # def derive(self, word_b: str, pos_b: str=None, pos_a: str=None, rule_id: str=None) -> List[Tuple[str, str]]:
    def derive(self, word_b: str, pos_b: str = None, pos_a: str = None, rule_id: str = None) -> List[str]:
        # tags = self.tag_guesser.guess(word=word_b, pos_b=pos_b)
        results = list()
        if pos_a is None:
            for pos_a_ in all_pos:
                if pos_b is None:
                    new_results = []
                    for pos_b_ in all_pos:
                        new_results.extend(self.derive_with_pos(word_b=word_b, pos_b=pos_b_, pos_a=pos_a_,
                                                                rule_id=rule_id))
                else:
                    new_results = self.derive_with_pos(word_b=word_b, pos_b=pos_b, pos_a=pos_a_, rule_id=rule_id)
                results.extend(new_results)
        else:
            if pos_b is None:
                new_results = []
                for pos_b_ in all_pos:
                    new_results.extend(self.derive_with_pos(word_b=word_b, pos_b=pos_b_, pos_a=pos_a, rule_id=rule_id))
            else:
                new_results = self.derive_with_pos(word_b=word_b, pos_b=pos_b, pos_a=pos_a, rule_id=rule_id)
            results.extend(new_results)
        return list(set(results))


"""
d = Derivation()
t = set(d.derive('ядерный', 'adj', 'adj'))
for elem in t:
    print(elem)
"""
