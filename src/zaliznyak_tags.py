from src.functions import *

"""
Морфотеги для существительных: pos|gender|number|animacy|template, где
pos = noun,
gender in {f, m, n},
number in {s, p}, # single vs. plural
animacy in {a, ina}, # одуш, неодуш
template in {1, ..., 8}

Морфотеги для прилагательных: pos|gender|form|animacy|template, где
pos = noun,
gender in {f, m, n, p},  # genders + plural
form in {f, s}, # полная, краткая
animacy in {a, ina}, # одуш, неодуш
template in {1, ..., 8}
"""

all_name_types = {

    # 1 — слова с основой на твёрдый согласный (топор, комод, балда, кобра, олово, пекло; твёрдый, тусклый)

    Rule('Zaliznyak_noun|f|s|.|1', 'noun|f|s|.|1', '', "(delsfx, {'а'}) & (onlysfx, consonants - morphobad)"),
    Rule('Zaliznyak noun|f|p|.|1', 'noun|f|p|.|1', '', "(delsfx, {'ы'}) & (onlysfx, consonants - morphobad)"),

    Rule('Zaliznyak noun|m|s|.|1', 'noun|m|s|.|1', '', "(onlysfx, consonants - morphobad)"),
    Rule('Zaliznyak noun|m|p|.|1', 'noun|m|p|.|1', '', "(delsfx, {'ы'}) & (onlysfx, consonants - morphobad)"),

    Rule('Zaliznyak noun|n|s|.|1', 'noun|n|s|.|1', '',
         "(delsfx, {'о'}) & (onlysfx, {'ы'} | consonants - morphobad)"),
    Rule('Zaliznyak noun|n|p|.|1', 'noun|n|p|.|1', '',
         "(delsfx, {'а'}) & (onlysfx, {'ы'} | consonants - morphobad)"),

    Rule('Zaliznyak ', 'adj|m|f|.|1', '', "(delsfx, {'ый', 'ой'}) & (onlysfx, consonants - morphobad)"),

    # 2 — слова с основой на мягкий согласный (тюлень, искатель, цапля, Дуня, горе, поле; весенний)

    Rule('Zaliznyak noun|f|s|.|2', 'noun|f|s|.|2', '', "(delsfx, {'я'}) & (onlysfx, consonants - morphobad)"),
    Rule('Zaliznyak noun|f|p|.|2', 'noun|f|p|.|2', '', "(delsfx, {'и'}) & (onlysfx, consonants - morphobad)"),

    Rule('Zaliznyak noun|m|s|.|2', 'noun|m|s|.|2', '',
         "(excsfx, {'путь'}) & (delsfx, {'ь'}) & (onlysfx, consonants - morphobad)"),
    Rule('Zaliznyak noun|m|p|.|2', 'noun|m|p|.|2', '',
         "(excsfx, {'пути'}) & (delsfx, {'и'}) & (onlysfx, consonants - morphobad)"),

    Rule('Zaliznyak noun|n|s|.|2', 'noun|n|s|.|2', '',
         "(delsfx, {'е'}) & (onlysfx, all_letters - morphobad - {'и', 'ь'})"),
    Rule('Zaliznyak noun|n|p|.|2', 'noun|n|p|.|2', '',
         "(delsfx, {'я'}) & (onlysfx, all_letters - morphobad - {'и', 'ь'})"),

    Rule('Zaliznyak ', 'adj|m|f|.|2', '', "(delsfx, {'ий'}) & (onlysfx, consonants - morphobad)"),


    # 3 — слова с основой на г, к или х (сапог, коряга, парк, моллюск, золотко, петух, неряха; мягкий)

    Rule('Zaliznyak noun|f|s|.|3', 'noun|f|s|.|3', '', "(delsfx, {'а'}) & (onlysfx, velar)"),
    Rule('Zaliznyak noun|f|p|.|3', 'noun|f|p|.|3', '', "(delsfx, {'и'}) & (onlysfx, velar)"),

    Rule('Zaliznyak noun|m|s|.|3', 'noun|m|s|.|3', '', "(onlysfx, velar)"),
    Rule('Zaliznyak noun|m|p|.|3', 'noun|m|p|.|3', '', "(delsfx, {'и'}) & (onlysfx, velar)"),

    Rule('Zaliznyak noun|n|s|.|3', 'noun|n|s|.|3', '', "(delsfx, {'о'}) & (onlysfx, velar)"),
    Rule('Zaliznyak noun|n|p|.|3', 'noun|n|p|.|3', '', "(delsfx, {'а', 'и'}) & (onlysfx, velar)"),

    Rule('Zaliznyak ', 'adj|m|f|.|3', '', "(delsfx, {'ый', 'ой', 'ий'}) & (onlysfx, velar)"),

    # 4 — слова с основой на ж, ш, ч, щ (калач, лаваш, галоша, святоша, жилище, вече, вящий)

    Rule('Zaliznyak noun|f|s|.|4', 'noun|f|s|.|4', '', "(delsfx, {'а'}) & (onlysfx, sh)"),
    Rule('Zaliznyak noun|f|p|.|4', 'noun|f|p|.|4', '', "(delsfx, {'и'}) & (onlysfx, sh)"),

    Rule('Zaliznyak noun|m|s|.|4', 'noun|m|s|.|4', '', "(onlysfx, sh)"),
    Rule('Zaliznyak noun|m|p|.|4', 'noun|m|p|.|4', '', "(delsfx, {'и'}) & (onlysfx, sh)"),

    Rule('Zaliznyak noun|n|s|.|4', 'noun|n|s|.|4', '', "(delsfx, {'е', 'о'}) & (onlysfx, sh)"),
    Rule('Zaliznyak noun|n|p|.|4', 'noun|n|p|.|4', '', "(delsfx, {'а', 'и'}) & (onlysfx, sh)"),

    Rule('Zaliznyak ', 'adj|m|f|.|4', '', "(delsfx, {'ой', 'ий'}) & (onlysfx, sh)"),

    # 5 — слова с основой на ц (немец, конец, девица, деревце, куцый)

    Rule('Zaliznyak noun|f|s|.|5', 'noun|f|s|.|5', '', "(delsfx, {'а'}) & (onlysfx, {'ц'})"),
    Rule('Zaliznyak noun|f|p|.|5', 'noun|f|p|.|5', '', "(delsfx, {'ы'}) & (onlysfx, {'ц'})"),

    Rule('Zaliznyak noun|m|s|.|5', 'noun|m|s|.|5', '', "(onlysfx, {'ц'})"),
    Rule('Zaliznyak noun|m|p|.|5', 'noun|m|p|.|5', '', "(delsfx, {'ы'}) & (onlysfx, {'ц'})"),

    Rule('Zaliznyak noun|n|s|.|5', 'noun|n|s|.|5', '', "(delsfx, {'е', 'о'}) & (onlysfx, {'ц'})"),
    Rule('Zaliznyak noun|n|p|.|5', 'noun|n|p|.|5', '', "(delsfx, {'а'}) & (onlysfx, {'ц'})"),

    Rule('Zaliznyak ', 'adj|m|f|.|5', '', "(delsfx, {'ый', 'ой'}) & (onlysfx, {'ц'})"),

    # 6 — слова с основой на гласный (кроме и) или й/j (бой, край; шея, здоровье)

    Rule('Zaliznyak noun|f|s|.|6', 'noun|f|s|.|6', '',
         "(delsfx, {'я'}) & (onlysfx, {'й', 'ь'} | vowels - {'и'})"),
    Rule('Zaliznyak noun|f|p|.|6', 'noun|f|p|.|6', '',
         "(delsfx, {'и'}) & (onlysfx, {'й', 'ь'} | vowels - {'и'})"),

    Rule('Zaliznyak noun|m|s|.|6', 'noun|m|s|.|6', '', "(delsfx, {'й'}) & (onlysfx, {'ь'} | vowels - {'и'})"),
    Rule('Zaliznyak noun|m|p|.|6', 'noun|m|p|.|6', '', "(delsfx, {'и'}) & (onlysfx, {'ь'} | vowels - {'и'})"),

    Rule('Zaliznyak noun|n|s|.|6', 'noun|n|s|.|6', '', "(onlysfx, {'ье', 'ьё'})"),
    Rule('Zaliznyak noun|n|p|.|6', 'noun|n|p|.|6', '', "(onlysfx, {'ья'})"),

    # 7 — слова с основой на и (полоний, сложение, мания, удостоверение)

    Rule('Zaliznyak noun|f|s|.|7', 'noun|f|s|.|7', '', "(onlysfx, {'ия'})"),
    Rule('Zaliznyak noun|f|p|.|7', 'noun|f|p|.|7', '', "(onlysfx, {'ии'})"),

    Rule('Zaliznyak noun|m|s|.|7', 'noun|m|s|.|7', '', "(onlysfx, {'ий'})"),
    Rule('Zaliznyak noun|m|p|.|7', 'noun|m|p|.|7', '', "(onlysfx, {'ии'})"),

    Rule('Zaliznyak noun|n|s|.|7', 'noun|n|s|.|7', '', "(onlysfx, {'ие'})"),
    Rule('Zaliznyak noun|n|p|.|7', 'noun|n|p|.|7', '', "(onlysfx, {'ия'})"),

    # 8 — слова с традиционным «3-м склонением» (боль, тетрадь, зыбь)

    Rule('Zaliznyak noun|f|s|.|8', 'noun|f|s|.|8', '', "(onlysfx, {'ь'})"),
    Rule('Zaliznyak noun|f|p|.|8', 'noun|f|p|.|8', '', "(onlysfx, {'и'})"),

    Rule('Zaliznyak noun|m|s|.|8', 'noun|m|s|.|8', '', "(onlysfx, {'путь'})"),
    Rule('Zaliznyak noun|m|p|.|8', 'noun|m|p|.|8', '', "(onlysfx, {'пути'})"),

    Rule('Zaliznyak noun|n|s|.|8', 'noun|n|s|.|8', '', "(onlysfx, {'мя'})"),
    Rule('Zaliznyak noun|n|p|.|8', 'noun|n|p|.|8', '', "(onlysfx, {'мена'})"),

}

"""
Для глаголов проверяются инфинитив и формы 1-го и 3-го лиц ед. ч.
Генерируется Tuple из трех списков с вариантами форм. Слово принадлежит заданному типу, если каждый элемент исходной
тройки принадлежит соответствующему списку.
"""

all_verb_types = {

    # 1

    (
        Rule('Zaliznyak verb|inf|1.1', 'verb|inf|1.1', '', "(onlysfx, {'ать'})"),
        Rule('Zaliznyak verb|1st|1.1', 'verb|1st|1.1', '', "(replsfx, {('ать', 'аю')})"),
        Rule('Zaliznyak verb|3rd|1.1', 'verb|3rd|1.1', '', "(replsfx, {('ать', 'ает')})"),
    ),
    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|1.2', '', "(onlysfx, {'ять'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|1.2', '', "(replsfx, {('ять', 'яю')})"),
        Rule('Zaliznyak v 1 3rd', 'verb|3rd|1.2', '', "(replsfx, {('ять', 'яет')})"),
    ),
    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|1.3', '', "(onlysfx, {'еть'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|1.3', '', "(replsfx, {('еть', 'ею')})"),
        Rule('Zaliznyak v 1 3rd', 'verb|3rd|1.3', '', "(replsfx, {('еть', 'еет')})"),
    ),

    # 2

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|2.1', '', "(onlysfx, {'овать'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|2.1', '', "(replsfx, {('овать', 'ую')})"),
        Rule('Zaliznyak v 1 3rd', 'verb|3rd|2.1', '', "(replsfx, {('овать', 'ует')})"),
    ),

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|2.2', '', "(delsfx, {'евать'}) & (onlysfx, sh | {'ц'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|2.2', '', "(delsfx, {'евать'}) & (onlysfx, sh | {'ц'}) & (addsfx, {'ую'})"),
        Rule('Zaliznyak v 1 3rd', 'verb|3rd|2.2', '', "(delsfx, {'евать'}) & (onlysfx, sh | {'ц'}) & (addsfx, {'ует'})"),
    ),

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|2.3', '', "(delsfx, {'евать'}) & (excsfx, sh | {'ц'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|2.3', '', "(delsfx, {'евать'}) & (excsfx, sh | {'ц'}) & (onlysfx, {'юю'})"),
        Rule('Zaliznyak v 1 3rd', 'verb|3rd|2.3', '', "(delsfx, {'евать'}) & (excsfx, sh | {'ц'}) & (onlysfx, {'юет'})"),
    ),

    # 3

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|3', '', "(onlysfx, {'нуть'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|3', '', "(replsfx, {('нуть', 'ну')})"),
        Rule('Zaliznyak v 1 3rd', 'verb|3rd|3', '', "(replsfx, {('нуть', 'нет')})"),
    ),

    # 4

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|4', '', "(onlysfx, {'ить'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|4', '', "(delsfx, {'ить'}) & (try altcons) & [(onlysfx, sh) & "
                                                    "(addsfx, {'у'}) | (excsfx, sh) & (addsfx, {'ю'})]"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|4', '', "(replsfx, {('ить', 'ит')})"),
    ),

    # 5

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|5.1', '', "(onlysfx, {'ать'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|5.1', '', "(delsfx, {'ать'}) & (try altcons) & [(onlysfx, sh) & "
                                                      "(addsfx, {'у'}) | (excsfx, sh) & (addsfx, {'ю'})]"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|5.1', '', "(replsfx, {('ать', 'ит')})"),
    ),

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|5.2', '', "(onlysfx, {'ять'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|5.2', '', "(delsfx, {'ять'}) & (try altcons) & [(onlysfx, sh) & "
                                                      "(addsfx, {'у'}) | (excsfx, sh) & (addsfx, {'ю'})]"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|5.2', '', "(replsfx, {('ять', 'ит')})"),
    ),

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|5.3', '', "(onlysfx, {'еть'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|5.3', '', "(delsfx, {'еть'}) & (try altcons) & [(onlysfx, sh) & "
                                                      "(addsfx, {'у'}) | (excsfx, sh) & (addsfx, {'ю'})]"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|5.3', '', "(replsfx, {('еть', 'ит')})"),
    ),


    # 6

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|6.1', '', "(onlysfx, {'ать'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|6.1', '', "(delsfx, {'ать'}) & (try altcons) & [(onlysfx, sh) & "
                                                      "(addsfx, {'у'}) | (excsfx, sh) & (addsfx, {'ю'})]"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|6.1', '', "(delsfx, {'ать'}) & (try altcons) & (addsfx({'ет'}))"),
    ),

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|6.2', '', "(onlysfx, {'ять'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|6.2', '', "(delsfx, {'ять'}) & (try altcons) & [(onlysfx, sh) & "
                                                      "(addsfx, {'у'}) | (excsfx, sh) & (addsfx, {'ю'})]"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|6.2', '', "(delsfx, {'ять'}) & (try altcons) & (addsfx({'ет'}))"),
    ),

    # 7

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|7.1', '', "(onlysfx, {'зти', 'зть'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|7.1', '', "(delsfx, {'зти', 'зть'}) & (addsfx, {'зу'})"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|7.1', '', "(delsfx, {'зти', 'зть'}) & (addsfx, {'зет'})"),
    ),

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|7.2', '', "(onlysfx, {'сти', 'сть'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|7.2', '', "(delsfx, {'сти', 'сть'}) & (addsfx, {'су'})"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|7.2', '', "(delsfx, {'сти', 'сть'}) & (addsfx, {'сет'})"),
    ),

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|7.3', '', "(onlysfx, {'сти', 'сть'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|7.3', '', "(delsfx, {'сти', 'сть'}) & (addsfx, {'ду'})"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|7.3', '', "(delsfx, {'сти', 'сть'}) & (addsfx, {'дет'})"),
    ),

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|7.4', '', "(onlysfx, {'сти', 'сть'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|7.4', '', "(delsfx, {'сти', 'сть'}) & (addsfx, {'ту'})"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|7.4', '', "(delsfx, {'сти', 'сть'}) & (addsfx, {'тет'})"),
    ),

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|7.5', '', "(onlysfx, {'сти', 'сть'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|7.5', '', "(delsfx, {'сти', 'сть'}) & (addsfx, {'сту'})"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|7.5', '', "(delsfx, {'сти', 'сть'}) & (addsfx, {'стет'})"),
    ),

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|7.6', '', "(onlysfx, {'сти', 'сть'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|7.6', '', "(delsfx, {'сти', 'сть'}) & (addsfx, {'бу'})"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|7.6', '', "(delsfx, {'сти', 'сть'}) & (addsfx, {'бет'})"),
    ),

    # 8

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|8.1', '', "(onlysfx, {'чь'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|8.1', '', "(delsfx, {'чь'}) & (opt delvowel) & (addsfx, {'гу'})"),  # жгу
        Rule('Zaliznyak v 1 1st', 'verb|3rd|8.1', '', "(delsfx, {'чь'}) & (opt delvowel) & (addsfx, {'жёт'})"),
    ),

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|8.2', '', "(onlysfx, {'чь'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|8.2', '', "(replsfx, {('чь', 'ку')})"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|8.2', '', "(replsfx, {('чь', 'чёт')})"),
    ),

    # 9

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|9', '', "(onlysfx, {'ереть'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|9', '', "(replsfx, {('ереть', 'ру')})"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|9', '', "(replsfx, {('ереть', 'рёт')})"),
    ),

    # 10

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|10.1', '', "(onlysfx, {'ороть'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|10.1', '', "(replsfx, {('ороть', 'орю')})"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|10.1', '', "(replsfx, {('ороть', 'орет')})"),
    ),

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|10.2', '', "(onlysfx, {'олоть'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|10.2', '', "(replsfx, {('олоть', 'олю')})"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|10.2', '', "(replsfx, {('олоть', 'олет')})"),
    ),

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|10.3', '', "(onlysfx, {'олоть'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|10.3', '', "(replsfx, {('олоть', 'елю')})"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|10.3', '', "(replsfx, {('олоть', 'елет')})"),
    ),

    # 11

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|11', '', "(onlysfx, {'ить'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|11', '', "(replsfx, {('ить', 'ью')})"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|11', '', "(replsfx, {('ьть', 'ьёт')})"),
    ),

    # 12

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|12.1', '', "(onlysfx, {'ыть'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|12.1', '', "(replsfx, {('ыть', 'ою')})"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|12.1', '', "(replsfx, {('ыть', 'оет')})"),
    ),

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|12.2', '', "(onlysfx, {'уть'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|12.2', '', "(replsfx, {('уть', 'ую')})"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|12.2', '', "(replsfx, {('уть', 'ует')})"),
    ),

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|12.3', '', "(onlysfx, {'ить'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|12.3', '', "(replsfx, {('ить', 'ию')})"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|12.3', '', "(replsfx, {('ить', 'иет')})"),
    ),

    # 13

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|13', '', "(onlysfx, {'авать'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|13', '', "(replsfx, {('авать', 'аю')})"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|13', '', "(replsfx, {('авать', 'аёт')})"),
    ),

    # 14

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|14.1', '', "(onlysfx, {'ать', 'ять'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|14.1', '', "(delsfx, {'ать', 'ять'}) & (addsfx, {'ну'})"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|14.1', '', "(delsfx, {'ать', 'ять'}) & (addsfx, {'нет'})"),
    ),

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|14.2', '', "(onlysfx, {'ать', 'ять'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|14.2', '', "(delsfx, {'ать', 'ять'}) & (addsfx, {'му'})"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|14.2', '', "(delsfx, {'ать', 'ять'}) & (addsfx, {'мет'})"),
    ),

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|14.3', '', "(onlysfx, {'ать', 'ять'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|14.3', '', "(delsfx, {'ать', 'ять'}) & (addsfx, {'иму'})"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|14.3', '', "(delsfx, {'ать', 'ять'}) & (addsfx, {'имет'})"),
    ),

    # 15

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|15', '', "(onlysfx, {'ть'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|15', '', "(delsfx, {'ть'}) & (addsfx, {'ну'})"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|15', '', "(delsfx, {'ть'}) & (addsfx, {'нет'})"),
    ),

    # 16

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|16', '', "(onlysfx, {'ть'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|16', '', "(delsfx, {'ть'}) & (addsfx, {'ву'})"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|16', '', "(delsfx, {'ть'}) & (addsfx, {'вет'})"),
    ),

}


def acc_type(word: str, morphotags: str) -> List:
    tags = morphotags.split('|')
    pos = tags[0]
    if pos == 'noun':
        gender, number, animacy, template = tags[1:]
    elif pos == 'adj':
        gender, form, animacy, template = tags[1:]
    good_vars = list()
    for rule_for_type in all_name_types:
        rule_tags = rule_for_type.pos_b.split('|')
        rule_pos = rule_tags[0]
        if pos == rule_pos:
            if len(rule_for_type.apply(word)) > 0:
                good_vars.append(rule_for_type.pos_b)
    return good_vars


print(acc_type('широчайший', 'adj|.|.|.|.'))
