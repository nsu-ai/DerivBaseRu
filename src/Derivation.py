import os

from src.guesser.ZaliznyakGuesser import *


class Derivation:
    def __init__(self, use_guesser: bool = False, **kwargs):
        self.use_guesser = use_guesser
        if self.use_guesser:
            self.tag_guesser = ZaliznyakGuesser(**kwargs)
        self.pos_all = ['noun', 'adj', 'verb', 'adv']
        self.rules = []
        for pos in self.pos_all:
            derivation_rules = os.path.join(os.path.dirname(__file__), 'rules', 'rules_{}.json'.format(pos))
            if not os.path.isfile(derivation_rules):
                continue
            self.rules.extend(load_rules_from_json(derivation_rules, 'b'))

    @staticmethod
    def _derive_with_all_tags(self, word_b: str, pos_b: str, pos_a: str, rule: WholeRule, is_extended: bool = False,
                              **kwargs):
        results = list()
        if rule.pos_b == pos_b and rule.pos_a == pos_a:
            if pos_b == 'verb':
                if 'inflect_type' in kwargs:
                    for subrule in rule.subrules:
                        if set(kwargs['inflect_type']) & set(subrule.tags_b['inflect_type']):
                            results.extend(subrule.apply(word_b))
                else:
                    results.extend(rule.apply(word_b))
            elif pos_b == 'noun' or pos_b == 'adj':
                if 'inflect_type' in kwargs and 'gender' in kwargs:
                    for subrule in rule.subrules:
                        if set(kwargs['inflect_type']) & set(subrule.tags_b['inflect_type']) \
                                and set(kwargs['gender']) & set(subrule.tags_b['gender']):
                            results.extend(subrule.apply(word_b))
                else:
                    results.extend(rule.apply(word_b))
            elif pos_b == 'adv':
                results.extend(rule.apply(word_b))
            else:
                raise ValueError(f'Unexpected pos_b: {pos_b}.')

        results = list(set(results))
        if is_extended:
            return [(rule.name, results)]
        else:
            return results

    def _derive_with_rule(self, word_b: str, pos_b: str, pos_a: str, rule: WholeRule, is_extended: bool = False,
                          **kwargs):
        results = []
        pos_b_all = [pos_b] if pos_b is not None else self.pos_all
        pos_a_all = [pos_a] if pos_a is not None else self.pos_all
        for pos_b_ in pos_b_all:
            for pos_a_ in pos_a_all:
                results.extend(self._derive_with_all_tags(word_b, pos_b_, pos_a_, rule, is_extended, **kwargs))
        return results

    def _derive(self, word_b: str, pos_b: str, pos_a: str, rule: WholeRule, is_extended: bool = False, **kwargs):
        results = []
        if rule is not None:
            results.extend(self._derive_with_rule(word_b, pos_b, pos_a, rule, is_extended, **kwargs))
        else:
            for rule_ in self.rules:
                results.extend(self._derive_with_rule(word_b, pos_b, pos_a, rule_, is_extended, **kwargs))
        return results

    def derive(self, word_b: str, pos_b: str = None, pos_a: str = None, rule_id: str = None, is_extended: bool = False,
               **kwargs):
        if self.use_guesser:
            tags_all = self.tag_guesser.guess(word=word_b, pos=pos_b, **kwargs)
        else:
            tags_all = [dict()]

        rule = None
        if rule_id:
            # TODO: access by key for O(log(N)) using dict
            for rule_ in self.rules:
                if rule_.name == rule_id:
                    rule = rule_

        results = []
        for tags in tags_all:
            tags.update(**kwargs)
            results.extend(self._derive(word_b, pos_b, pos_a, rule, is_extended, **tags))
        return results
