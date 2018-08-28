import json
from src.Rule import *


class ZaliznyakGuesser:
    def __init__(self):
        with open('src/rules/rules_inflection.json', encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
        self.rules = list()
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
        Rule('Zaliznyak v 1 1st', 'verb|3rd|6.1', '', "(delsfx, {'ать'}) & (try altcons) & (addsfx, {'ет'})"),
    ),

    (
        Rule('Zaliznyak v 1 inf', 'verb|inf|6.2', '', "(onlysfx, {'ять'})"),
        Rule('Zaliznyak v 1 1st', 'verb|1st|6.2', '', "(delsfx, {'ять'}) & (try altcons) & [(onlysfx, sh) & "
                                                      "(addsfx, {'у'}) | (excsfx, sh) & (addsfx, {'ю'})]"),
        Rule('Zaliznyak v 1 1st', 'verb|3rd|6.2', '', "(delsfx, {'ять'}) & (try altcons) & (addsfx, {'ет'})"),
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
        Rule('Zaliznyak v 1 1st', 'verb|3rd|11', '', "(replsfx, {('ить', 'ьёт')})"),
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

