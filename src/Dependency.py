from copy import deepcopy
from typing import List, Set, Tuple, Dict


class DependencyToken:
    def __init__(self,
                 lemma: str,
                 pos: str,
                 label: str = 'root',
                 form: str = None,
                 tags: str = '',
                 ):
        self.lemma = lemma
        self.pos = pos
        self.label = label
        self.form = form or lemma
        self.tags = set(tags.split('|'))

        self.parent = 0

    def __str__(self):
        return f'{self.lemma}\t{self.pos}\t{self.parent}\t{self.label}'

    def __repr__(self):
        return self.__str__()


class DependencyTree:
    def __init__(self, tokens: List[DependencyToken], word: str = None):
        # inner or outer
        self.tokens = tokens
        for i, token in enumerate(self.tokens):
            if token.parent == 0:
                self.root = i
                self.root_outer = i
                self.root_inner = i
        self.pos = self.tokens[self.root_inner].pos
        self.word = word

    def __str__(self):
        lines = [f'# {self.word}\t{self.pos}'] + list(
            map(lambda ix: f'{ix[0] + 1}\t{ix[1].__str__()}', enumerate(self.tokens)))
        return '\n'.join(lines)

    def __repr__(self):
        return self.__str__()

    def set_word(self, word: str):
        self.word = word

    # simple and complex rules
    def add_token(self, token: DependencyToken, connection='inner', power='middle'):
        """
        :param token:
        :param connection: inner or outer
        :param power: strong, middle or weak
        strong changes the part of speech, weak does not
        weak examples: inflectional tags
        [weak]: x(o) y(i) + z -> x(o) y(i) z
        [middle]: x(o) y(i) + z -> x(o) y z(i)
        [strong]: x(o) y(i) + z -> x y z(o,i)
        examples: cat --> cats = [cat, Pl.]. Pl. here is weak outer
        :return:
        """
        token = deepcopy(token)
        token.position = len(self.tokens)

        if connection == 'outer':
            token.parent = self.root_outer + 1
        else:  # inner
            token.parent = self.root_inner + 1

        if power == 'strong':
            self.root_outer = token.position
            self.root_inner = token.position
            self.pos = token.pos
        elif power == 'middle':
            self.root_inner = token.position
            self.pos = token.pos
        else:  # weak
            pass

        self.tokens.append(token)

    def merge(self, other, arc_label, is_arc_l2r=True, connection='inner', power='weak'):
        n_tokens = len(self.tokens)
        for t in other.tokens:
            if t.parent > 0:
                t.parent += n_tokens
            self.tokens.append(t)

        if is_arc_l2r:
            self.tokens[other.root + n_tokens].label = arc_label
            if connection == 'inner':
                self.tokens[other.root + n_tokens].parent = self.root_inner + 1
            else:
                self.tokens[other.root + n_tokens].parent = self.root_outer + 1

            if power == 'strong':
                self.root_outer = other.root_outer + n_tokens
                self.root_inner = other.root_inner + n_tokens
            elif power == 'middle':
                self.root_inner = other.root_inner + n_tokens
            else:
                pass
        else:
            self.tokens[self.root].label = arc_label
            if connection == 'inner':
                self.tokens[self.root].parent = other.root_inner + 1 + len(self.tokens)
            else:
                self.tokens[self.root].parent = other.root_outer + 1 + len(self.tokens)

            if power == 'strong':
                self.root_outer = other.root_outer + n_tokens
                self.root_inner = other.root_inner + n_tokens
            elif power == 'middle':
                self.root_inner = other.root_inner + n_tokens
            else:
                pass