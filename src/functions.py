from typing import List, Set, Tuple, Dict

all_pos = {'noun', 'adj', 'adj*', 'verb', 'adv', 'num'}

paired = {'б', 'п', 'м', 'в', 'ф', 'д', 'т', 'з', 'с', 'н', 'л', 'р'}
velar = {'г', 'к', 'х'}
sh_hard = {'ш', 'ж'}
sh_soft = {'щ', 'ч'}

voiced = {'б', 'м', 'в', 'д', 'з', 'н', 'л', 'р', 'г', 'ж'}
unvoiced = {'п', 'ф', 'т', 'с', 'к', 'х', 'ш', 'ч', 'щ', 'ц'}

plt_pairs = ({('к', 'ч'), ('г', 'ж'), ('х', 'ш')})
inv_plt_pairs = ({('ч', 'к'), ('ж', 'г'), ('ш', 'х')})

plt5_pairs = ({('ц', 'ч')})
inv_plt5_pairs = ({('ч', 'ц')})

alt7_pairs = ({('е', 'о')})


altcons_pairs = ({('б', 'бл'), ('п', 'пл'), ('в', 'вл'), ('ф', 'фл'), ('м', 'мл'), ('з', 'ж'), ('с', 'ш'), ('д', 'ж'),
                  ('т', 'ч'), ('т', 'щ'), ('ст', 'щ'), ('к', 'ч'), ('г', 'ж'), ('х', 'ш'), ('ск', 'щ')})

inv_altcons_pairs = ({('бл', 'б'), ('пл', 'п'), ('вл', 'в'), ('фл', 'ф'), ('мл', 'м'), ('ж', 'з'), ('ш', 'с'),
                      ('ж', 'д'), ('ч', 'т'), ('щ', 'т'), ('щ', 'ст'), ('ч', 'к'), ('ж', 'г'), ('ш', 'х'),
                      ('щ', 'ск')})

vowels = {'а', 'о', 'у', 'ы', 'и', 'э', 'я', 'ё', 'ю', 'е'}
double_vowels = {'я', 'ё', 'ю', 'е'}

sh = sh_hard | sh_soft

consonants = paired | velar | sh_hard | sh_soft

morphobad = velar | sh_hard | sh_soft | {'ц'}

all_letters = consonants | vowels | {'ъ', 'ь'}


def nochange(word: str, args: Set[str], mode='do'):
    return [word]


def onlysfx(word: str, args: Set[str], mode='do'):
    sfx_b_ = args
    possible_results = list()

    for sfx_b in sfx_b_:
        if mode == 'do':
            if word.endswith(sfx_b):
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
            if word.endswith(sfx_b):
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
        for sfx_b, sfx_a in pairs:
            if word.endswith(sfx_b):
                # возможно изменение -> изменяем
                possible_word = word[:-len(sfx_b)] + sfx_a
                possible_results.append(possible_word)
    elif mode == 'try':
        counter = 0
        for sfx_b, sfx_a in pairs:
            if word.endswith(sfx_b):
                counter += 1
                # возможно изменение -> изменяем
                possible_word = word[:-len(sfx_b)] + sfx_a
                possible_results.append(possible_word)
        if counter == 0:
            # невозможно изменение -> не страшно
            possible_results.append(word)

    elif mode == 'opt':
        for sfx_b, sfx_a in pairs:
            if word.endswith(sfx_b):
                # возможно изменение -> изменяем или не изменяем
                possible_word = word[:-len(sfx_b)] + sfx_a
                possible_results.append(possible_word)
            possible_results.append(word)

    return possible_results


def addsfx(word: str, args: Set[str], mode='do'):
    sfx_a_ = args
    possible_results = list()

    for sfx_a in sfx_a_:
        possible_word = word + sfx_a
        possible_results.append(possible_word)

        if mode == 'opt':
            possible_results.append(word)

    return possible_results


def delsfx(word: str, args: Set[str], mode='do'):
    sfx_b_ = args
    possible_results = list()

    if mode == 'do':
        for sfx_b in sfx_b_:
            if word.endswith(sfx_b):
                # возможно изменение -> изменяем
                w_a = word[:-len(sfx_b)]
                possible_word = w_a
                possible_results.append(possible_word)
    elif mode == 'try':
        for sfx_b in sfx_b_:
            if word.endswith(sfx_b):
                # возможно изменение -> изменяем
                w_a = word[:-len(sfx_b)]
                possible_word = w_a
                possible_results.append(possible_word)
        # невозможно изменение -> не страшно
        if not possible_results:
            w_a = word
            possible_word = w_a
            possible_results.append(possible_word)
    elif mode == 'opt':
        for sfx_b in sfx_b_:
            if word.endswith(sfx_b):
                # возможно изменение -> изменяем или не изменяем
                w_a = word[:-len(sfx_b)]
                possible_word = w_a
                possible_results.append(possible_word)
            w_a = word
            possible_word = w_a
            possible_results.append(possible_word)

    return possible_results

def del_n(word: str, args: Set[str], mode='do'):
    # разнообразн|ый -> разнообраз|ить
    if len(word) < 3 or word[-1] != 'н' or word[-2] in vowels:
        if mode == 'do':
            return []
        else:
            return [word]

    w_a = word[:-1]
    if w_a.endswith('ь'):
        w_a = w_a[:-1]
    if mode == 'opt':
        return [word, w_a]
    else:
        return [w_a]

def del_k(word: str, args: Set[str], mode='do'):
    # крепк|ий -> креп|ить
    if len(word) < 3 or word[-1] != 'к' or word[-2] in vowels:
        if mode == 'do':
            return []
        else:
            return [word]

    w_a = word[:-1]
    if w_a.endswith('ь'):
        w_a = w_a[:-1]
    if mode == 'opt':
        return [word, w_a]
    else:
        return [w_a]


def atleast3(word: str, args: Set[str], mode='do'):
    # ! п|ировать -> п|ант
    # эмигр|ировать -> эмигр|ант
    if len(word) < 3:
        if mode == 'do':
            return []
        else:
            return [word]

def uppercase(word: str, args: Set[str], mode='do'):
    w_a = word[0].upper() + word[1:]
    if mode == 'opt':
        return [w_a, word]
    else:
        return [w_a]

def lowercase(word: str, args: Set[str], mode='do'):
    w_a = word.lower()
    if mode == 'opt':
        return [w_a, word]
    else:
        return [w_a]


def delptfx(word: str, args: Set[str], mode='do'):
    return delsfx(word, {'ся', 'сь'}, mode)


def delvowel(word: str, args: Set[str], mode='do'):
    if len(word) < 3:
        if mode == 'do':
            return []
        else:
            return [word]
    
    possible_results = list()
    
    if mode == 'do':
        if word[-2] in {'о', 'е'} and word[-3] in consonants:
            # возможно изменение -> изменяем
            w_a = word[:-2]
            if w_a.endswith('л'):
                w_a += 'ь'
            possible_word = w_a + word[-1]
            possible_results.append(possible_word)

    elif mode == 'try':
        if word[-2] in {'о', 'е'} and word[-3] in consonants:
            # возможно изменение -> изменяем
            w_a = word[:-2]
            if w_a.endswith('л'):
                w_a += 'ь'
            possible_word = w_a + word[-1]
            possible_results.append(possible_word)
        else:
            # невозможно изменение -> не страшно
            w_a = word
            possible_word = w_a
            possible_results.append(possible_word)

    elif mode == 'opt':
        if word[-2] in {'о', 'е'} and word[-3] in consonants:
            # возможно изменение -> изменяем
            w_a = word[:-2]
            if w_a.endswith('л'):
                w_a += 'ь'
            possible_word = w_a + word[-1]
            possible_results.append(possible_word)
        w_a = word
        possible_word = w_a
        possible_results.append(possible_word)

    return possible_results


def addvowel(word: str, args: Set[str], mode='do'):
    if len(word) < 3:
        if mode == 'do':
            return []
        else:
            return [word]
    
    possible_results = list()
    
    w_a = word[:-1]
    if w_a[-1] == 'ь':
        w_a = w_a[:-1]
    if w_a[-1] == 'й':
        possible_word = w_a[:-1] + 'е' + word[-1]
        possible_results.append(possible_word)
    elif w_a[-1] in consonants:
        for add_vowel in {'о', 'е'}:
            possible_word = w_a + add_vowel + word[-1]
            possible_results.append(possible_word)

    if mode == 'opt' or (mode == 'try' and not possible_results):
        w_a = word
        possible_word = w_a
        possible_results.append(possible_word)

    return possible_results


def plt(word: str, args: Set[str], mode='do'):
    return replsfx(word, plt_pairs, mode)


def inv_plt(word: str, args: Set[str], mode='do'):
    return replsfx(word, inv_plt_pairs, mode)


def plt5(word: str, args: Set[str], mode='do'):
    return replsfx(word, plt5_pairs, mode)


def inv_plt5(word: str, args: Set[str], mode='do'):
    return replsfx(word, inv_plt5_pairs, mode)


def altcons(word: str, args: Set[str], mode='do'):
    return replsfx(word, altcons_pairs, mode)


def inv_altcons(word: str, args: Set[str], mode='do'):
    return replsfx(word, inv_altcons_pairs, mode)


def l_soft(word: str, args: Set[str], mode='do'):
    return replsfx(word, ({('л', 'ль')}), mode)


def l_hard(word: str, args: Set[str], mode='do'):
    return replsfx(word, ({('ль', 'л')}), mode)


def alt_a(word: str, args: Set[str], mode='do'):
    # выкорм|ить -> выкарм|ливать
    possible_results = list()

    if mode == 'opt':
        possible_results.append(word)

    for i in range(len(word) - 1, -1, -1):
        if word[i] == 'о':
            w_a = word[:i] + 'а' + word[i + 1:]
            possible_word = w_a
            possible_results.append(possible_word)
            return possible_results
    if mode == 'try':
        possible_results.append(word)
    return possible_results


def alt7(word: str, args: Set[str], mode='do'):
    # вывести -> вывод
    possible_results = list()

    if mode == 'opt':
        possible_results.append(word)

    for i in range(len(word) - 1, -1, -1):
        if word[i] == 'е':
            w_a = word[:i] + 'о' + word[i + 1:]
            possible_word = w_a
            possible_results.append(possible_word)
            return possible_results
    if mode == 'try':
        possible_results.append(word)
    return possible_results


def alt_pfx(word: str, args: Set[str], mode='do'):
    possible_results = list()

    if mode == 'opt':
        possible_results.append(word)

    if word[0] == 'и':
        w_a = 'ы' + word[1:]
        possible_word = w_a
        possible_results.append(possible_word)
    elif word[0] in double_vowels:
        w_a = 'ъ' + word
        possible_word = w_a
        possible_results.append(possible_word)
    else:
        possible_results.append(word)
    return possible_results


def alt_pfxi(word: str, args: Set[str], mode='do'):
    possible_results = list()

    if mode == 'opt':
        possible_results.append(word)

    if word[0] in double_vowels:
        w_a = 'ъ' + word
        possible_word = w_a
        possible_results.append(possible_word)
    else:
        possible_results.append(word)
    return possible_results


def ins_pfx(word: str, args: Set[str], mode='do'):
    # only for prefixes like из, раз, без, ...
    possible_results = list()

    pfx_a = list(args)[0]

    if mode == 'opt':
        possible_results.append(word)

    if pfx_a.endswith('з'):
        if word[0] in unvoiced:
            w_a = pfx_a[:-1] + 'с' + word
            possible_word = w_a
            possible_results.append(possible_word)
        else:
            w_a = pfx_a + word
            possible_word = w_a
            possible_results.append(possible_word)
        return possible_results
    else:
        if mode == 'do':
            return possible_results
        else:
            possible_results.append(word)
            return possible_results


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


def replpfx(word: str, args: Set[Tuple[str, str]], mode='do'):
    pairs = args
    possible_results = list()

    if mode == 'do':
        for pair in pairs:
            pfx_b, pfx_a = pair
            if word[:len(pfx_b)] == pfx_b:
                # возможно изменение -> изменяем
                w_a = word[len(pfx_b):]
                possible_word = pfx_a + w_a
                possible_results.append(possible_word)
    elif mode == 'try':
        counter = 0
        for pair in pairs:
            pfx_b, pfx_a = pair
            if word[:len(pfx_b)] == pfx_b:
                counter += 1
                # возможно изменение -> изменяем
                w_a = word[len(pfx_b):]
                possible_word = pfx_a + w_a
                possible_results.append(possible_word)
        if counter == 0:
            # невозможно изменение -> не страшно
            w_a = word
            possible_word = w_a
            possible_results.append(possible_word)

    elif mode == 'opt':
        for pair in pairs:
            pfx_b, pfx_a = pair
            if word[:len(pfx_b)] == pfx_b:
                # возможно изменение -> изменяем или не изменяем
                w_a = word[len(pfx_b):]
                possible_word = pfx_a + w_a
                possible_results.append(possible_word)
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


def hard(word: str, args: Set[str], mode='do'):
    possible_results = list()

    w_a = word
    if w_a.endswith('ь'):
        possible_word = w_a[:-1]
        possible_results.append(possible_word)
    elif mode == 'try':
        possible_results.append(word)

    if mode == 'opt':
        w_a = word
        possible_word = w_a
        possible_results.append(possible_word)

    return possible_results


def excpfx(word: str, args: Set[str], mode='do'):
    pfx_b_ = args
    possible_results = list()

    counter = 0
    for pfx_b in pfx_b_:
        if mode == 'do':
            if word[:len(pfx_b)] == pfx_b:
                continue
            else:
                counter += 1
        else:
            possible_results.append(word)

    if counter == len(pfx_b_):
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
