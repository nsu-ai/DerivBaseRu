from typing import List, Set, Tuple
from lark.tree import pydot__tree_to_png

from src.loading_rules_to_tree import *


paired = {'б', 'п', 'м', 'в', 'ф', 'д', 'т', 'з', 'с', 'н', 'л', 'р'}
velar = {'г', 'к', 'х'}
sh_hard = {'ш', 'ж'}
sh_soft = {'щ', 'ч'}

voiced = {'б', 'м', 'в', 'д', 'з', 'н', 'л', 'р', 'г', 'ж'}
unvoiced = {'п', 'ф', 'т', 'с', 'к', 'х', 'ш', 'ч', 'щ'}

plt_pairs = ({('к', 'ч'), ('г', 'ж'), ('х', 'ш')})

altcons_pairs = ({('б', 'бл'), ('п', 'пл'), ('в', 'вл'), ('ф', 'фл'), ('м', 'мл'), ('з', 'ж'), ('с', 'ш'), ('д', 'ж'),
                  ('т', 'ч'), ('т', 'щ'), ('ст', 'щ'), ('к', 'ч'), ('г', 'ж'), ('х', 'ш'), ('ск', 'щ')})

vowels = {'а', 'о', 'у', 'ы', 'и', 'э', 'я', 'ё', 'ю', 'е'}

sh = sh_hard | sh_soft

consonants = paired | velar | sh_hard | sh_soft

morphobad = velar | sh_hard | sh_soft | {'ц'}

all_letters = consonants | vowels | {'ъ', 'ь'}


def onlysfx(word: str, args: Set[str], mode='do'):
    sfx_b_ = args
    possible_results = list()

    for sfx_b in sfx_b_:
        if mode == 'do':
            if word[-len(sfx_b):] == sfx_b:
                possible_results.append(word)
        else:
            possible_results.append(word)

    return possible_results


def excsfx(word: str, args: Set[str], mode='do'):
    sfx_b_ = args
    possible_results = list()

    counter = 0
    for sfx_b in sfx_b_:
        if mode == 'do':
            if word[-len(sfx_b):] == sfx_b:
                continue
            else:
                counter += 1
        else:
            possible_results.append(word)

    if counter == len(sfx_b_):
        possible_results.append(word)

    return possible_results


def replsfx(word: str, args: Set[Tuple[str, str]], mode='do'):
    pairs = args
    possible_results = list()

    if mode == 'do':
        for pair in pairs:
            sfx_b, sfx_a = pair
            if word[-len(sfx_b):] == sfx_b:
                # возможно изменение -> изменяем
                w_a = word[:-len(sfx_b)]
                possible_word = w_a + sfx_a
                possible_results.append(possible_word)
    elif mode == 'try':
        counter = 0
        for pair in pairs:
            sfx_b, sfx_a = pair
            if word[-len(sfx_b):] == sfx_b:
                counter += 1
                # возможно изменение -> изменяем
                w_a = word[:-len(sfx_b)]
                possible_word = w_a + sfx_a
                possible_results.append(possible_word)
        if counter == 0:
            # невозможно изменение -> не страшно
            w_a = word
            possible_word = w_a
            possible_results.append(possible_word)

    elif mode == 'opt':
        for pair in pairs:
            sfx_b, sfx_a = pair
            if word[-len(sfx_b):] == sfx_b:
                # возможно изменение -> изменяем или не изменяем
                w_a = word[:-len(sfx_b)]
                possible_word = w_a + sfx_a
                possible_results.append(possible_word)
            w_a = word
            possible_word = w_a
            possible_results.append(possible_word)

    return possible_results


def addsfx(word: str, args: Set[str], mode='do'):
    sfx_a_ = args
    possible_results = list()

    w_a = word
    for sfx_a in sfx_a_:
        possible_word = w_a + sfx_a
        possible_results.append(possible_word)

        if mode == 'opt':
            w_a = word
            possible_word = w_a
            possible_results.append(possible_word)

    return possible_results


def delsfx(word: str, args: Set[str], mode='do'):
    sfx_b_ = args
    possible_results = list()

    for sfx_b in sfx_b_:
        if mode == 'do':
            if word[-len(sfx_b):] == sfx_b:
                # возможно изменение -> изменяем
                w_a = word[:-len(sfx_b)]
                possible_word = w_a
                possible_results.append(possible_word)

        elif mode == 'try':
            if word[-len(sfx_b):] == sfx_b:
                # возможно изменение -> изменяем
                w_a = word[:-len(sfx_b)]
                possible_word = w_a
                possible_results.append(possible_word)
            else:
                # невозможно изменение -> не страшно
                w_a = word
                possible_word = w_a
                possible_results.append(possible_word)

        elif mode == 'opt':
            if word[-len(sfx_b):] == sfx_b:
                # возможно изменение -> изменяем или не изменяем
                w_a = word[:-len(sfx_b)]
                possible_word = w_a
                possible_results.append(possible_word)
            w_a = word
            possible_word = w_a
            possible_results.append(possible_word)

    return possible_results


def delvowel(word: str, args: Set[str], mode='do'):
    possible_results = list()

    if mode == 'do':
        if word[-2] in {'о', 'е'}:
            # возможно изменение -> изменяем
            w_a = word[:-2]
            possible_word = w_a + word[-1]
            possible_results.append(possible_word)

    elif mode == 'try':
        if word[-2] in {'о', 'е'}:
            # возможно изменение -> изменяем
            w_a = word[:-2]
            possible_word = w_a + word[-1]
            possible_results.append(possible_word)
        else:
            # невозможно изменение -> не страшно
            w_a = word
            possible_word = w_a
            possible_results.append(possible_word)

    elif mode == 'opt':
        if word[-2] in {'о', 'е'}:
            # возможно изменение -> изменяем
            w_a = word[:-2]
            possible_word = w_a + word[-1]
            possible_results.append(possible_word)
        w_a = word
        possible_word = w_a
        possible_results.append(possible_word)

    return possible_results


def addvowel(word: str, args: Set[str], mode='do'):
    possible_results = list()

    w_a = word[:-1]
    if w_a[-1] == 'ь':
        w_a = w_a[:-1]
    for add_vowel in {'о', 'е', 'и'}:
        possible_word = w_a + add_vowel + word[-1]
        possible_results.append(possible_word)

    if mode == 'opt':
        w_a = word
        possible_word = w_a
        possible_results.append(possible_word)

    return possible_results


def plt(word: str, args: Set[str], mode='do'):
    return replsfx(word, plt_pairs, mode)


def altcons(word: str, args: Set[str], mode='do'):
    return replsfx(word, altcons_pairs, mode)


def addpfx(word: str, args: Set[str], mode='do'):
    pfx_a_ = args
    possible_results = list()

    w_a = word
    for pfx_a in pfx_a_:
        possible_word = pfx_a + w_a
        possible_results.append(possible_word)

        if mode == 'opt':
            w_a = word
            possible_word = w_a
            possible_results.append(possible_word)

    return possible_results


def soft(word: str, args: Set[str], mode='do'):
    possible_results = list()

    w_a = word
    possible_word = w_a + 'ь'
    possible_results.append(possible_word)

    if mode == 'opt':
        w_a = word
        possible_word = w_a
        possible_results.append(possible_word)

    return possible_results


def excpfx(word: str, args: Set[str], mode='do'):
    pfx_b_ = args
    possible_results = list()

    for pfx_b in pfx_b_:
        if mode == 'do':
            if word[:len(pfx_b)] == pfx_b:
                continue
        else:
            possible_results.append(word)

    return possible_results


def onlypfx(word: str, args: Set[str], mode='do'):
    pfx_b_ = args
    possible_results = list()

    for pfx_b in pfx_b_:
        if mode == 'do':
            if word[:len(pfx_b)] == pfx_b:
                possible_results.append(word)
        else:
            possible_results.append(word)

    return possible_results


class Rule:
    def __init__(self, id: str, pos_b: str, pos_a: str, raw_rules: str):
        self.id = id
        self.pos_b = pos_b
        self.pos_a = pos_a
        self.logical_form, self.operators = normalize_raw_text(raw_rules)
        self.tree = short_parser.parse(self.logical_form)

    def plot_tree(self, filename: str='tree'):
        pydot__tree_to_png(self.tree, filename + ".png")

    def compute_tree(self, tree, cur_results: List[str]):
        # leaf
        if hasattr(tree.children[0], 'value'):
            command = self.operators[int(tree.children[0].value)]
            # print(command)
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

    def apply(self, word: str):
        results = self.compute_tree(self.tree, [word])
        return results
