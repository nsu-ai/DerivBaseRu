from src.Dependency import DependencyToken, DependencyTree
from src.Rule import WholeRule, ComplexRule


class DependencyWord(DependencyTree):
    def __init__(self, word: str, pos: str):
        super().__init__([DependencyToken(word, pos)], word=word)

    def add_rule(self, rule: WholeRule, word: str = None):
        if isinstance(rule, ComplexRule):
            self.add_complex(rule, word)
        elif isinstance(rule, WholeRule):
            self.add_simple(rule, word)

    def merge_(self, other, arc_label, is_arc_l2r=True, connection='inner', power='weak'):
        self.merge(other, arc_label, is_arc_l2r, connection, power)

    def add_simple(self, rule: WholeRule, word: str = None, connection=None, power=None):
        if rule.info == 'SFX':
            if rule.pos_a != rule.pos_b:
                self.add_token(DependencyToken(rule.short_id, rule.pos_a, label=f'pos:{rule.pos_b}>{rule.pos_a}'),
                               connection=connection or 'outer', power=power or 'strong')
            else:
                self.add_token(DependencyToken(rule.short_id, rule.pos_a, label=f'mod:{rule.pos_b}'),
                               connection=connection or 'outer', power=power or 'weak')
        elif rule.info == 'PTFX':
            self.add_token(DependencyToken(rule.short_id, rule.pos_a, label=f'mod:{rule.pos_b}'),
                           connection=connection or 'outer', power=power or 'weak')
        elif rule.info == 'PFX':
            self.add_token(DependencyToken(rule.short_id, rule.pos_a, label=f'mod:{rule.pos_b}'),
                           connection=connection or 'inner', power=power or 'middle')
        elif rule.info == 'CONV':
            self.add_token(DependencyToken(rule.short_id, rule.pos_a, label=f'conv:{rule.pos_b}>{rule.pos_a}'),
                           connection=connection or 'inner', power=power or 'weak')
        else:
            raise AssertionError('Rule info is incorrect!', rule.name, rule.info)

        if word:
            self.word = word

    def add_complex(self, rule: ComplexRule, word: str=None):
        for subrule in rule.simple_rules:
            self.add_simple(subrule)

        if word:
            self.word = word

