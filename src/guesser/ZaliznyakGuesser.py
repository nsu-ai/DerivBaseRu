import os
import json
from itertools import chain as chain
from functools import reduce
from src.Rule import *
"""
converter_of_verb_types = {'1а': '1', '1я': '1', '1е': '1',
                           '2о': '2', '2е*': '2', '2е': '2',
                           '5а': '5', '5я': '5', '5е': '5',
                           '5ща': '5щ', '5щя': '5щ', '5ще': '5щ',
                           '6а': '6', '6я': '6',
                           '6ща': '6щ', '6щя': '6щ',
                           }
"""
converter_of_verb_types = {'1а': '1', '1я': '1', '1е': '1',
                           '2о': '2', '2е*': '2', '2е': '2',
                           '4щ': '4',
                           '5а': '5', '5я': '5', '5е': '5',
                           '5ща': '5', '5щя': '5', '5ще': '5',
                           '6а': '6', '6я': '6',
                           '6ща': '6', '6щя': '6',
                           }

order_of_verb_types = {'1': 1,
                       '2': 1,
                       '3': 1,
                       '4щ': 1, '4': 2,
                       '5щ': 1, '5': 2,
                       '6щ': 1, '6': 2,
                       '7з': 1, '7б': 1, '7с': 1, '7д': 1, '7т': 1, '7ст': 1,
                       '8г': 1, '8к': 1, '8*3': 1,
                       '9': 1,
                       '10ор': 1, '10ел': 1, '10ол': 1,
                       '11': 1,
                       '12ы': 1, '12у': 1, '12и': 1, '12греть': 1, '12брить': 1, '12петь': 1,
                       '13': 1,
                       '14н': 1, '14м': 1, '14ним': 1, '14ьм': 1, '14ым': 1, '14им': 1, '14йм': 1,
                       '15': 2,
                       '16': 1,
                       }


class ZaliznyakGuesser:
    def __init__(self):
        if os.path.dirname(os.getcwd()).endswith('src'):
            inflection_rules = os.path.join(os.path.dirname(os.getcwd()), 'rules', 'rules_inflection.json')
        elif os.path.dirname(os.getcwd()).endswith('DerivBaseRu'):
            inflection_rules = os.path.join(os.path.dirname(os.getcwd()), 'src', 'rules', 'rules_inflection.json')
        else:
            inflection_rules = os.path.join(os.path.dirname(os.getcwd()), 'DerivBaseRu', 'src', 'rules', 'rules_inflection.json')
        print(inflection_rules)
        with open(inflection_rules, encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
        self.rules = dict()
        for json_rule in data['data']:
            new_rules = list()
            rule_id = json_rule['rule_id']
            pos_b = json_rule['pos_b']
            pos_a = pos_b
            rule_info = ''
            for case in json_rule['cases']:
                name = rule_id + ':' + case['case_id']
                tags_a = case['tags_a']
                raw_rules = case['rules']
                new_case = Rule(name=name, pos_b=pos_b, pos_a=pos_a, tags_b=tags_a, raw_rules=raw_rules,
                                info=rule_info)
                new_rules.append(new_case)
            self.rules[pos_b] = new_rules

    def guess_single_word_with_pos(self, word: str, pos_b: str, **kwargs) -> List[Dict[str, str]]:
        if pos_b not in self.rules:
            return []
        possible_variants = list()
        for rule in self.rules[pos_b]:
            if len(rule.apply(word)) > 0:
                possible_variants.append(rule.tags_b)
        return possible_variants

    def guess(self, pos_b: str = None, **kwargs) -> List[Dict[str, str]]:
        possible_variants = list()
        if pos_b is None:
            for pos in all_pos - {'verb'}:
                possible_variants.extend(self.guess_single_word_with_pos(pos_b=pos, **kwargs))
            possible_variants.extend(self.guess_verb(pos_b='verb', **kwargs))
        else:
            if pos_b != 'verb':
                possible_variants.extend(self.guess_single_word_with_pos(pos_b=pos_b, **kwargs))
            else:
                possible_variants.extend(self.guess_verb(pos_b='verb', **kwargs))
        return possible_variants

    def guess_verb(self, inf: str, per1: str, per3: str, pos_b: str = 'verb', **kwargs) -> List[Dict[str, str]]:
        possible_variants = []
        for verb_form, verb_tag in [(inf, 'inf'), (per1, 'per1'), (per3, 'per3')]:
            form_vars = self.guess_single_word_with_pos(verb_form, pos_b)
            possible_variants.append(
                set(chain.from_iterable([elem['inflect_type'] for elem in form_vars if verb_tag in elem['form']])))
        possible_variants = reduce(lambda x, y: x & y, possible_variants)
        possible_variants = list(set(map(lambda x: converter_of_verb_types.setdefault(x, x), possible_variants)))
        possible_variants.sort(key=lambda x: order_of_verb_types[x])
        possible_variants = [{'pos_b': 'verb', 'inflect_type': [x]} for x in possible_variants]
        return possible_variants


"""
z = ZaliznyakGuesser()
r = z.guess(word='мыло', pos_b='noun')
print(r)
"""
