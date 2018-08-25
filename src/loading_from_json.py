import json
from src.functions import *


with open('package.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

all_rules = list()
for json_rule in data['data']:
    new_rule = Rule(json_rule['id'], json_rule['pos_b'], json_rule['pos_a'], json_rule['rules'])
    # print(new_rule.id, new_rule.logical_form)
    all_rules.append(new_rule)

words = ['дед', 'Игорь', 'Сергей', 'царь', 'бригадир', 'учитель']  # 611
words = ['мама', 'сестра', 'Володя', 'колдунья']  # 612
words = ['человек', 'мужик', 'казак', 'вдова', 'внук', 'птица', 'баран', 'рыба']  # 614


for rule in all_rules:
    if rule.id == 'rule614':
        print(rule.id)
        for word in words:
            print(list(set(rule.apply(word))))
