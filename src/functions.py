class Rule:
    def __init__(self, pos_b, pos_a, rules):
        self.pos_b = pos_b
        self.pos_a = pos_a
        self.rules = rules


class POS:
    def __init__(self, gr: str, pos: str, history=list()):
        self.pos = pos
        self.graphics = gr
        self.history = history


class Derivation:
    def __init__(self):
        self.ok = True

    def apply_changing(self, word: POS, rule, pos_b, pos_a):
        cur_vars = [word]
        f, argums = rule[0], rule[1:]
        mode = 'do'
        if argums[0] in {'do', 'try', 'opt'}:
            mode = argums[0]
            argums = argums[1:]
        cur_vars_new = []
        for cur_var in cur_vars:
            cur_vars_new += f(cur_var, argums, pos_b, pos_a, mode=mode)
        cur_vars = cur_vars_new

        return cur_vars

    def parse_rule(self, word: POS, rules, pos_b, pos_a):
        cur_vars = [word]
        if isinstance(rules, tuple) and (not isinstance(rules[0], tuple) and not isinstance(rules[0], list)):
            return self.apply_changing(word, rules, pos_b, pos_a)
        elif isinstance(rules, tuple) and (isinstance(rules[0], tuple) or isinstance(rules[0], list)):
            new_vars = []
            for r in rules:
                new_vars += self.parse_rule(word, r, pos_b, pos_a)
            return new_vars
        elif isinstance(rules, list):
            for r in rules:
                new_vars = []
                for cur_var in cur_vars:
                    new_vars += self.parse_rule(cur_var, r, pos_b, pos_a)
                cur_vars = new_vars
            return cur_vars

    def apply_pattern(self, word: POS, a_rule: Rule):
        pos_b, pos_a = a_rule.pos_b, a_rule.pos_a
        res_vars = self.parse_rule(word, a_rule.rules, pos_b, pos_a)

        return res_vars


paired = {'б', 'п', 'м', 'в', 'ф', 'д', 'т', 'з', 'с', 'н', 'л', 'р'}
velar = {'г', 'к', 'х'}
sh_hard = {'ш', 'ж'}
sh_soft = {'щ', 'ч'}

voiced = {'б', 'м', 'в', 'д', 'з', 'н', 'л', 'р', 'г', 'ж'}
unvoiced = {'п', 'ф', 'т', 'с', 'к', 'х', 'ш', 'ч', 'щ'}

plt_pairs = ({('к', 'ч'), ('г', 'ж'), ('х', 'ш')})

vowels = {'а', 'о', 'у', 'ы', 'и', 'э', 'я', 'ё', 'ю', 'е'}

sh = sh_hard | sh_soft

consonants = paired | velar | sh_hard | sh_soft


def replsfx(word: POS, args, pos_b, pos_a, mode='do'):
    if isinstance(args, set):
        pairs = args
    else:
        pairs = args[0]
    possible_results = list()

    if mode == 'do':
            for pair in pairs:
                sfx_b, sfx_a = pair
            if word.graphics[-len(sfx_b):] == sfx_b:
                # возможно изменение -> изменяем
                w_a = word.graphics[:-len(sfx_b)]
                possible_word = w_a + sfx_a
                new_word = POS(possible_word, pos_a, word.history)
                possible_results.append(new_word)
    elif mode == 'try':
        counter = 0
        for pair in pairs:
            sfx_b, sfx_a = pair
            if word.graphics[-len(sfx_b):] == sfx_b:
                counter += 1
                # возможно изменение -> изменяем
                w_a = word.graphics[:-len(sfx_b)]
                possible_word = w_a + sfx_a
                new_word = POS(possible_word, pos_a, word.history)
                possible_results.append(new_word)
        if counter == 0:
            # невозможно изменение -> не страшно
            w_a = word.graphics
            possible_word = w_a
            new_word = POS(possible_word, pos_a, word.history)
            possible_results.append(new_word)

    elif mode == 'opt':
        for pair in pairs:
            sfx_b, sfx_a = pair
            if word.graphics[-len(sfx_b):] == sfx_b:
                # возможно изменение -> изменяем или не изменяем
                w_a = word.graphics[:-len(sfx_b)]
                possible_word = w_a + sfx_a
                new_word = POS(possible_word, pos_a, word.history)
                possible_results.append(new_word)
            w_a = word.graphics
            possible_word = w_a
            new_word = POS(possible_word, pos_a, word.history)
            possible_results.append(new_word)

    return possible_results


def addsfx(word: POS, args, pos_b, pos_a, mode='do'):
    sfx_a_ = args[0]
    possible_results = list()

    w_a = word.graphics
    for sfx_a in sfx_a_:
        possible_word = w_a + sfx_a
        new_word = POS(possible_word, pos_a, word.history)
        possible_results.append(new_word)

        if mode == 'opt':
            w_a = word.graphics
            possible_word = w_a
            new_word = POS(possible_word, pos_a, word.history)
            possible_results.append(new_word)

    return possible_results


def delsfx(word: POS, args, pos_b, pos_a, mode='do'):
    sfx_b_ = args[0]
    possible_results = list()

    for sfx_b in sfx_b_:
        if mode == 'do':
            if word.graphics[-len(sfx_b):] == sfx_b:
                # возможно изменение -> изменяем
                w_a = word.graphics[:-len(sfx_b)]
                possible_word = w_a
                new_word = POS(possible_word, pos_a, word.history)
                possible_results.append(new_word)

        elif mode == 'try':
            if word.graphics[-len(sfx_b):] == sfx_b:
                # возможно изменение -> изменяем
                w_a = word.graphics[:-len(sfx_b)]
                possible_word = w_a
                new_word = POS(possible_word, pos_a, word.history)
                possible_results.append(new_word)
            else:
                # невозможно изменение -> не страшно
                w_a = word.graphics
                possible_word = w_a
                new_word = POS(possible_word, pos_a, word.history)
                possible_results.append(new_word)

        elif mode == 'opt':
            if word.graphics[-len(sfx_b):] == sfx_b:
                # возможно изменение -> изменяем или не изменяем
                w_a = word.graphics[:-len(sfx_b)]
                possible_word = w_a
                new_word = POS(possible_word, pos_a, word.history)
                possible_results.append(new_word)
            w_a = word.graphics
            possible_word = w_a
            new_word = POS(possible_word, pos_a, word.history)
            possible_results.append(new_word)

    return possible_results


def excsfx(word: POS, args, pos_b, pos_a, mode='do'):
    sfx_b_ = args[0]
    possible_results = list()

    counter = 0
    for sfx_b in sfx_b_:
        if mode == 'do':
            if word.graphics[-len(sfx_b):] == sfx_b:
                continue
            else:
                counter += 1
        else:
            possible_results.append(word)

    if counter == len(sfx_b_):
        possible_results.append(word)

    return possible_results


def onlysfx(word: POS, args, pos_b, pos_a, mode='do'):
    sfx_b_ = args[0]
    possible_results = list()

    for sfx_b in sfx_b_:
        if mode == 'do':
            if word.graphics[-len(sfx_b):] == sfx_b:
                possible_results.append(word)
        else:
            possible_results.append(word)

    return possible_results


def delvowel(word: POS, args, pos_b, pos_a, mode='do'):
    possible_results = list()

    if mode == 'do':
        if word.graphics[-2] in {'о', 'е'}:
            # возможно изменение -> изменяем
            w_a = word.graphics[:-2]
            possible_word = w_a + word.graphics[-1]
            new_word = POS(possible_word, pos_a, word.history)
            possible_results.append(new_word)

    elif mode == 'try':
        if word.graphics[-2] in {'о', 'е'}:
            # возможно изменение -> изменяем
            w_a = word.graphics[:-2]
            possible_word = w_a + word.graphics[-1]
            new_word = POS(possible_word, pos_a, word.history)
            possible_results.append(new_word)
        else:
            # невозможно изменение -> не страшно
            w_a = word.graphics
            possible_word = w_a
            new_word = POS(possible_word, pos_a, word.history)
            possible_results.append(new_word)

    elif mode == 'opt':
        if word.graphics[-2] in {'о', 'е'}:
            # возможно изменение -> изменяем
            w_a = word.graphics[:-2]
            possible_word = w_a + word.graphics[-1]
            new_word = POS(possible_word, pos_a, word.history)
            possible_results.append(new_word)
        w_a = word.graphics
        possible_word = w_a
        new_word = POS(possible_word, pos_a, word.history)
        possible_results.append(new_word)

    return possible_results


def addvowel(word: POS, args, pos_b, pos_a, mode='do'):
    possible_results = list()

    w_a = word.graphics[:-1]
    if w_a[-1] == 'ь':
        w_a = w_a[:-1]
    for add_vowel in {'о', 'е', 'и'}:
        possible_word = w_a + add_vowel + word.graphics[-1]
        new_word = POS(possible_word, pos_a, word.history)
        possible_results.append(new_word)

    if mode == 'opt':
        w_a = word.graphics
        possible_word = w_a
        new_word = POS(possible_word, pos_a, word.history)
        possible_results.append(new_word)

    return possible_results


def plt(word: POS, args, pos_b, pos_a, mode='do'):
    return replsfx(word, plt_pairs, pos_b, pos_a, mode)


def addpfx(word: POS, args, pos_b, pos_a, mode='do'):
    pfx_a_ = args[0]
    possible_results = list()

    w_a = word.graphics
    for pfx_a in pfx_a_:
        possible_word = pfx_a + w_a
        new_word = POS(possible_word, pos_a, word.history)
        possible_results.append(new_word)

        if mode == 'opt':
            w_a = word.graphics
            possible_word = w_a
            new_word = POS(possible_word, pos_a, word.history)
            possible_results.append(new_word)

    return possible_results


def soft(word: POS, args, pos_b, pos_a, mode='do'):
    possible_results = list()

    w_a = word.graphics
    possible_word = w_a + 'ь'
    new_word = POS(possible_word, pos_a, word.history)
    possible_results.append(new_word)

    if mode == 'opt':
        w_a = word.graphics
        possible_word = w_a
        new_word = POS(possible_word, pos_a, word.history)
        possible_results.append(new_word)

    return possible_results


def excpfx(word: POS, args, pos_b, pos_a, mode='do'):
    pfx_b_ = args[0]
    possible_results = list()

    for pfx_b in pfx_b_:
        if mode == 'do':
            if word.graphics[:len(pfx_b)] == pfx_b:
                continue
        else:
            possible_results.append(word)

    return possible_results


def onlypfx(word: POS, args, pos_b, pos_a, mode='do'):
    pfx_b_ = args[0]
    possible_results = list()

    for pfx_b in pfx_b_:
        if mode == 'do':
            if word.graphics[:len(pfx_b)] == pfx_b:
                possible_results.append(word)
        else:
            possible_results.append(word)

    return possible_results

