from lark.tree import pydot__tree_to_png

from src.loading_rules_to_tree import *
from src.functions import *


class Rule:
    def __init__(self, name: str, pos_b: str, pos_a: str, tags_b: Dict[str, str], raw_rules: str):
        self.name = name
        self.pos_a = pos_a
        self.tags_b = dict()
        self.tags_b['pos_b'] = pos_b
        for tag in tags_b:
            possible_values = tags_b[tag].split(',')
            self.tags_b[tag] = possible_values
        self.logical_form, self.operators = normalize_raw_text(raw_rules)
        self.tree = short_parser.parse(self.logical_form)

    def plot_tree(self, filename: str='tree'):
        pydot__tree_to_png(self.tree, filename + ".png")

    def compute_tree(self, tree, cur_results: List[str]) -> List[str]:
        # leaf
        if hasattr(tree.children[0], 'value'):
            command = self.operators[int(tree.children[0].value)]
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

    def apply(self, word: str) -> List[str]:
        results = self.compute_tree(self.tree, [word])
        return results
