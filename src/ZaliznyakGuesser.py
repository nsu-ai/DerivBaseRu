import os
import glob
import json
from src.Rule import *


class ZaliznyakGuesser:
    def __init__(self):
        inflection_rules = os.path.join(os.path.dirname(__file__), 'rules', 'rules_inflection.json')
        with open(inflection_rules, encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
        self.rules = dict()
        for json_rule in data['data']:
            new_rules = list()
            rule_id = json_rule['rule_id']
            pos_b = json_rule['pos_b']
            pos_a = pos_b
            for case in json_rule['cases']:
                name = rule_id + ':' + case['case_id']
                tags_a = case['tags_a']
                raw_rules = case['rules']
                new_case = Rule(name=name, pos_b=pos_b, pos_a=pos_a, tags_b=tags_a, raw_rules=raw_rules)
                new_rules.append(new_case)
            self.rules[pos_b] = new_rules

    def guess_with_pos(self, word: str, pos_b: str) -> List[Dict[str, List[str]]]:
        if pos_b not in self.rules:
            return []
        possible_variants = list()
        for rule in self.rules[pos_b]:
            if len(rule.apply(word)) > 0:
                possible_variants.append(rule.tags_b)
        return possible_variants

    def guess(self, word: str, pos_b: str=None) -> List[Dict[str, List[str]]]:
        possible_variants = list()
        if pos_b is None:
            for pos in all_pos:
                possible_variants.extend(self.guess_with_pos(word, pos))
        else:
            possible_variants.extend(self.guess_with_pos(word, pos_b))
        return possible_variants