import os

from src.guesser.ZaliznyakGuesser import *


class Derivation:
    def __init__(self, use_guesser: bool = False):
        self.use_guesser = use_guesser
        if self.use_guesser:
            self.tag_guesser = ZaliznyakGuesser()
        self.rules = list()
        for pos in ['noun', 'adj', 'verb', 'adv']:
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

                if 'info' not in json_rule:
                    print(rule_id)
                for case in json_rule['cases']:
                    name = rule_id + ':' + case['case_id']
                    tags_b = case['tags_b']
                    raw_rules = case['rules']
                    new_case = Rule(name=name, pos_b=pos_b, pos_a=pos_a, tags_b=tags_b, raw_rules=raw_rules,
                                    info=json_rule['info'])
                    new_rule.append(new_case)
                self.rules.extend(new_rule)

    def derive_with_tags(self, word_b: str, pos_b: str, pos_a: str, rule_id: str = None, **kwargs) -> List[str]:
        # {'pos_b': 'noun', 'gender': ['n'], 'number': ['s'], 'inflect_type': ['1']}
        results = list()
        if not rule_id:
            for rule in self.rules:
                if rule.tags_b['pos_b'] == pos_b and rule.pos_a == pos_a:
                    if pos_b == 'verb':
                        if set(kwargs['inflect_type']) & set(rule.tags_b['inflect_type']):
                            new_results = rule.apply(word_b)
                            for word_result in new_results:
                                # result = (word_result, rule.name)
                                results.append(word_result)
                    elif pos_b == 'noun' or pos_b == 'adj':
                        if set(kwargs['inflect_type']) & set(rule.tags_b['inflect_type']) and \
                                set(kwargs['gender']) & set(rule.tags_b['gender']):
                            new_results = rule.apply(word_b)
                            for word_result in new_results:
                                # result = (word_result, rule.name)
                                results.append(word_result)
                    else:
                        new_results = rule.apply(word_b)
                        for word_result in new_results:
                            # result = (word_result, rule.name)
                            results.append(word_result)

        else:
            for rule in self.rules:
                if rule.name != rule_id:
                    continue
                if rule.tags_b['pos_b'] == pos_b and rule.pos_a == pos_a:
                    if pos_b == 'verb':
                        if set(kwargs['inflect_type']) & set(rule.tags_b['inflect_type']):
                            new_results = rule.apply(word_b)
                            for word_result in new_results:
                                # result = (word_result, rule.name)
                                results.append(word_result)
                    elif pos_b == 'noun' or pos_b == 'adj':
                        if set(kwargs['inflect_type']) & set(rule.tags_b['inflect_type']) and \
                                set(kwargs['gender']) & set(rule.tags_b['gender']):
                            new_results = rule.apply(word_b)
                            for word_result in new_results:
                                # result = (word_result, rule.name)
                                results.append(word_result)
                    else:
                        new_results = rule.apply(word_b)
                        for word_result in new_results:
                            # result = (word_result, rule.name)
                            results.append(word_result)
        return results

    def derive_with_tags_ext(self, word_b: str, pos_b: str, pos_a: str, rule_id: str = None, **kwargs) -> List[Tuple[str, str]]:
        # {'pos_b': 'noun', 'gender': ['n'], 'number': ['s'], 'inflect_type': ['1']}
        results = list()

        if not rule_id:
            for rule in self.rules:
                try:
                    if rule.tags_b['pos_b'] == pos_b and rule.pos_a == pos_a:
                        if pos_b == 'verb':
                            if set(kwargs['inflect_type']) & set(rule.tags_b['inflect_type']):
                                new_results = rule.apply(word_b)
                                for word_result in new_results:
                                    # result = (word_result, rule.name)
                                    results.append((word_result, rule.name))
                        elif pos_b == 'noun' or pos_b == 'adj':
                            if set(kwargs['inflect_type']) & set(rule.tags_b['inflect_type']) and \
                                    set(kwargs['gender']) & set(rule.tags_b['gender']):
                                new_results = rule.apply(word_b)
                                for word_result in new_results:
                                    # result = (word_result, rule.name)
                                    results.append((word_result, rule.name))
                        else:
                            new_results = rule.apply(word_b)
                            for word_result in new_results:
                                # result = (word_result, rule.name)
                                results.append((word_result, rule.name))
                except:
                    print(rule.name, 'error occurred!')
        else:
            for rule in self.rules:
                if rule.name != rule_id:
                    continue
                if rule.tags_b['pos_b'] == pos_b and rule.pos_a == pos_a:
                    if pos_b == 'verb':
                        if set(kwargs['inflect_type']) & set(rule.tags_b['inflect_type']):
                            new_results = rule.apply(word_b)
                            for word_result in new_results:
                                # result = (word_result, rule.name)
                                results.append((word_result, rule.name))
                    elif pos_b == 'noun' or pos_b == 'adj':
                        if set(kwargs['inflect_type']) & set(rule.tags_b['inflect_type']) and \
                                set(kwargs['gender']) & set(rule.tags_b['gender']):
                            new_results = rule.apply(word_b)
                            for word_result in new_results:
                                # result = (word_result, rule.name)
                                results.append((word_result, rule.name))
                    else:
                        new_results = rule.apply(word_b)
                        for word_result in new_results:
                            # result = (word_result, rule.name)
                            results.append((word_result, rule.name))
        return results


    def derive_with_tags_node_ext(self, word_b: str, pos_b: str, pos_a: str, rule_id: str = None, **kwargs) -> List[Tuple[str, str]]:
        # {'pos_b': 'noun', 'gender': ['n'], 'number': ['s'], 'inflect_type': ['1']}
        results = list()

        if not rule_id:
            for rule in self.rules:
                if rule.tags_b['pos_b'] == pos_b and rule.pos_a == pos_a:
                    if pos_b == 'verb':
                        if set(kwargs['inflect_type']) & set(rule.tags_b['inflect_type']):
                            new_results = rule.apply(word_b)
                            for word_result in new_results:
                                # result = (word_result, rule.name)
                                results.append((word_result, rule.pos_a))
                    elif pos_b == 'noun' or pos_b == 'adj':
                        # print(rule.name)
                        if set(kwargs['inflect_type']) & set(rule.tags_b['inflect_type']) and \
                                set(kwargs['gender']) & set(rule.tags_b['gender']):
                            new_results = rule.apply(word_b)
                            for word_result in new_results:
                                # result = (word_result, rule.name)
                                results.append((word_result, rule.pos_a))
                    else:
                        new_results = rule.apply(word_b)
                        for word_result in new_results:
                            # result = (word_result, rule.name)
                            results.append((word_result, rule.pos_a))

        else:
            for rule in self.rules:
                if rule.name != rule_id:
                    continue
                if rule.tags_b['pos_b'] == pos_b and rule.pos_a == pos_a:
                    if pos_b == 'verb':
                        if set(kwargs['inflect_type']) & set(rule.tags_b['inflect_type']):
                            new_results = rule.apply(word_b)
                            for word_result in new_results:
                                # result = (word_result, rule.name)
                                results.append((word_result, rule.name))
                    elif pos_b == 'noun' or pos_b == 'adj':
                        if set(kwargs['inflect_type']) & set(rule.tags_b['inflect_type']) and \
                                set(kwargs['gender']) & set(rule.tags_b['gender']):
                            new_results = rule.apply(word_b)
                            for word_result in new_results:
                                # result = (word_result, rule.name)
                                results.append((word_result, rule.name))
                    else:
                        new_results = rule.apply(word_b)
                        for word_result in new_results:
                            # result = (word_result, rule.name)
                            results.append((word_result, rule.name))
        return results

    def derive_with_pos_ext(self, word_b: str, pos_b: str, pos_a: str, rule_id: str = None) -> List[Tuple[str, str]]:
        results = list()
        if not rule_id:
            for rule in self.rules:
                if rule.tags_b['pos_b'] == pos_b and rule.pos_a == pos_a:
                    try:
                        new_results = rule.apply(word_b)
                        for word_result in new_results:
                            results.append((word_result, rule.name))
                    except:
                        print(rule.name)
        else:
            for rule in self.rules:
                if rule.name != rule_id:
                    continue
                if rule.tags_b['pos_b'] == pos_b and rule.pos_a == pos_a:
                    new_results = rule.apply(word_b)
                    for word_result in new_results:
                        results.append((word_result, rule.name))
        return results

    def derive_with_pos_node_ext(self, word_b: str, pos_b: str, pos_a: str, rule_id: str = None, **kwargs) -> List[Tuple[str, str]]:
        results = list()
        if not rule_id:
            for rule in self.rules:
                if rule.tags_b['pos_b'] == pos_b and rule.pos_a == pos_a:
                    try:
                        new_results = rule.apply(word_b)
                        for word_result in new_results:
                            results.append((word_result, rule.pos_a))
                    except:
                        print(rule.name)
        else:
            for rule in self.rules:
                if rule.name != rule_id:
                    continue
                if rule.tags_b['pos_b'] == pos_b and rule.pos_a == pos_a:
                    new_results = rule.apply(word_b)
                    for word_result in new_results:
                        results.append((word_result, rule.pos_a))
        return results

    def derive_with_pos(self, word_b: str, pos_b: str, pos_a: str, rule_id: str = None) -> List[str]:
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

    def derive_wtags_node_ext(self, word_b: str, pos_b: str = None, pos_a: str = None, rule_id: str = None, **kwargs) -> List[Tuple[str, str]]:
        # tags = self.tag_guesser.guess(word=word_b, pos_b=pos_b)
        results = list()
        if pos_a is None:
            for pos_a_ in all_pos:
                if pos_b is None:
                    new_results = []
                    for pos_b_ in all_pos:
                        new_results.extend(self.derive_with_tags_node_ext(word_b=word_b, pos_b=pos_b_, pos_a=pos_a_,
                                                                         rule_id=rule_id, **kwargs))
                else:
                    new_results = self.derive_with_tags_node_ext(word_b=word_b, pos_b=pos_b, pos_a=pos_a_, rule_id=rule_id, **kwargs)
                results.extend(new_results)
        else:
            if pos_b is None:
                new_results = []
                for pos_b_ in all_pos:
                    new_results.extend(self.derive_with_tags_node_ext(word_b=word_b, pos_b=pos_b_, pos_a=pos_a, rule_id=rule_id, **kwargs))
            else:
                new_results = self.derive_with_tags_node_ext(word_b=word_b, pos_b=pos_b, pos_a=pos_a, rule_id=rule_id, **kwargs)
            results.extend(new_results)
        return list(set(results))

    def derive_node_ext(self, word_b: str, pos_b: str = None, pos_a: str = None, rule_id: str = None, **kwargs) -> List[Tuple[str, str]]:
        # tags = self.tag_guesser.guess(word=word_b, pos_b=pos_b)
        results = list()
        if pos_a is None:
            for pos_a_ in all_pos:
                if pos_b is None:
                    new_results = []
                    for pos_b_ in all_pos:
                        new_results.extend(self.derive_with_pos_node_ext(word_b=word_b, pos_b=pos_b_, pos_a=pos_a_,
                                                                         rule_id=rule_id, **kwargs))
                else:
                    new_results = self.derive_with_pos_node_ext(word_b=word_b, pos_b=pos_b, pos_a=pos_a_, rule_id=rule_id, **kwargs)
                results.extend(new_results)
        else:
            if pos_b is None:
                new_results = []
                for pos_b_ in all_pos:
                    new_results.extend(self.derive_with_pos_node_ext(word_b=word_b, pos_b=pos_b_, pos_a=pos_a, rule_id=rule_id, **kwargs))
            else:
                new_results = self.derive_with_pos_node_ext(word_b=word_b, pos_b=pos_b, pos_a=pos_a, rule_id=rule_id, **kwargs)
            results.extend(new_results)
        return list(set(results))

    def derive_ext(self, word_b: str, pos_b: str = None, pos_a: str = None, rule_id: str = None) -> List[Tuple[str, str]]:
        # tags = self.tag_guesser.guess(word=word_b, pos_b=pos_b)
        results = list()
        if pos_a is None:
            for pos_a_ in all_pos:
                if pos_b is None:
                    new_results = []
                    for pos_b_ in all_pos:
                        new_results.extend(self.derive_with_pos_ext(word_b=word_b, pos_b=pos_b_, pos_a=pos_a_,
                                                                    rule_id=rule_id))
                else:
                    new_results = self.derive_with_pos_ext(word_b=word_b, pos_b=pos_b, pos_a=pos_a_, rule_id=rule_id)
                results.extend(new_results)
        else:
            if pos_b is None:
                new_results = []
                for pos_b_ in all_pos:
                    new_results.extend(self.derive_with_pos_ext(word_b=word_b, pos_b=pos_b_, pos_a=pos_a, rule_id=rule_id))
            else:
                new_results = self.derive_with_pos_ext(word_b=word_b, pos_b=pos_b, pos_a=pos_a, rule_id=rule_id)
            results.extend(new_results)
        return list(set(results))

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

z = ZaliznyakGuesser()
v = 'вор'
r = z.guess(word=v, pos_b='noun')[0]
print(r)
t2 = set(d.derive_with_tags(v, pos_a='adv', **r))
print(len(t2))
for elem in t2:
    print(elem)
"""
