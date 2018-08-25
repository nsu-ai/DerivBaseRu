import json
from src.functions import *


with open('package.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

all_rules = list()
for json_rule in data['data']:
    new_rule = Rule(json_rule['id'], json_rule['pos_b'], json_rule['pos_a'], json_rule['rules'])
    print(new_rule.id, new_rule.logical_form)
    all_rules.append(new_rule)

import pandas as pd
df = pd.read_csv('wiki_ADV.csv')

advs_test = []
pos = 0
neg = 0

pos_examples = []
neg_examples = []

for i in range(df.shape[0]):
    s = df[i:i + 1].values[0]

    w_a = s[0].lower()
    w_b = s[1].lower()

    advs_test.append(w_a.replace('ё', 'е'))

    correct_generated = False

    pos_a = 'adv'

    ans = []

    # print(w_b)
    for rule in all_rules:
        if rule.pos_a == pos_a:
            print(rule.id)
            ans += rule.apply(w_b)

    for elem in ans:
        if elem.lower().replace('ё', 'е') == w_a.replace('ё', 'е'):
            correct_generated = True
    if correct_generated:
        pos += 1
        pos_examples.append(w_a)
    else:
        neg += 1
        neg_examples.append(w_a)

print(pos, neg)

for neg_ex in neg_examples:
    print(neg_ex)

print(pos / (neg + pos))