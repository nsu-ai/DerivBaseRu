import unittest

from src.Derivation import Derivation


class TestDerivationADJ(unittest.TestCase):
    def setUp(self):
        self.derivation = Derivation()

    def tearDown(self):
        del self.derivation

    def test_adj_611(self):
        results = self.derivation.derive(word_b='дед', pos_b='noun', pos_a='adj*')
        self.assertIn('дедов', results)
        results = self.derivation.derive(word_b='государь', pos_b='noun', pos_a='adj*')
        self.assertIn('государев', results)
        results = self.derivation.derive(word_b='пастух', pos_b='noun', pos_a='adj*')
        self.assertIn('пастухов', results)
        results = self.derivation.derive(word_b='царевич', pos_b='noun', pos_a='adj*')
        self.assertIn('царевичев', results)
        results = self.derivation.derive(word_b='отец', pos_b='noun', pos_a='adj*')
        self.assertIn('отцов', results)
        results = self.derivation.derive(word_b='Сергей', pos_b='noun', pos_a='adj*')
        self.assertIn('Сергеев', results)

    @unittest.skip
    def test_adj_611_2(self):
        results = self.derivation.derive(word_b='Довженко', pos_b='noun', pos_a='adj*')
        self.assertIn('Довженков', results)
        results = self.derivation.derive(word_b='Вивальди', pos_b='noun', pos_a='adj*')
        self.assertIn('Вивальдиев', results)

    @unittest.skip
    def test_adj_611_3(self):
        results = self.derivation.derive(word_b='Аврора', pos_b='noun', pos_a='adj*')
        self.assertIn('Авроров', results)
        results = self.derivation.derive(word_b='коммуна', pos_b='noun', pos_a='adj*')
        self.assertIn('коммунова', results)
        results = self.derivation.derive(word_b='одеяло', pos_b='noun', pos_a='adj*')
        self.assertIn('одеялово', results)

    def test_adj_612(self):
        results = self.derivation.derive(word_b='мама', pos_b='noun', pos_a='adj*')
        self.assertIn('мамин', results)
        results = self.derivation.derive(word_b='дядя', pos_b='noun', pos_a='adj*')
        self.assertIn('дядин', results)
        results = self.derivation.derive(word_b='бабушка', pos_b='noun', pos_a='adj*')
        self.assertIn('бабушкин', results)
        results = self.derivation.derive(word_b='директорша', pos_b='noun', pos_a='adj*')
        self.assertIn('директоршин', results)
        results = self.derivation.derive(word_b='синица', pos_b='noun', pos_a='adj*')
        self.assertIn('синицын', results)
        results = self.derivation.derive(word_b='Илья', pos_b='noun', pos_a='adj*')
        self.assertIn('Ильин', results)
        results = self.derivation.derive(word_b='матерь', pos_b='noun', pos_a='adj*')
        self.assertIn('материн', results)

    @unittest.skip
    def test_adj_612_2(self):
        results = self.derivation.derive(word_b='листик', pos_b='noun', pos_a='adj*')
        self.assertIn('листикин', results)
        results = self.derivation.derive(word_b='поэт', pos_b='noun', pos_a='adj*')
        self.assertIn('поэтин', results)

    @unittest.skip
    def test_adj_612_3(self):
        results = self.derivation.derive(word_b='Вилли', pos_b='noun', pos_a='adj*')
        self.assertIn('Виллин', results)
        results = self.derivation.derive(word_b='Мэри', pos_b='noun', pos_a='adj*')
        self.assertIn('Мэрин', results)

    @unittest.skip
    def test_adj_613(self):
        results = self.derivation.derive(word_b='брат', pos_b='noun', pos_a='adj*')
        self.assertIn('братнин', results)
        results = self.derivation.derive(word_b='муж', pos_b='noun', pos_a='adj*')
        self.assertIn('мужнин', results)
        results = self.derivation.derive(word_b='зять', pos_b='noun', pos_a='adj*')
        self.assertIn('зятнин', results)
        results = self.derivation.derive(word_b='дочерь', pos_b='noun', pos_a='adj*')
        self.assertIn('дочернин', results)

    def test_adj_614(self):
        results = self.derivation.derive(word_b='вдова', pos_b='noun', pos_a='adj*')
        self.assertIn('вдовий', results)
        results = self.derivation.derive(word_b='баран', pos_b='noun', pos_a='adj*')
        self.assertIn('бараний', results)
        results = self.derivation.derive(word_b='митрополит', pos_b='noun', pos_a='adj*')
        self.assertIn('митрополичий', results)

        results = self.derivation.derive(word_b='пескарь', pos_b='noun', pos_a='adj*')
        self.assertIn('пескарий', results)
        results = self.derivation.derive(word_b='человек', pos_b='noun', pos_a='adj*')
        self.assertIn('человечий', results)
        results = self.derivation.derive(word_b='медведь', pos_b='noun', pos_a='adj*')
        self.assertIn('медвежий', results)
        results = self.derivation.derive(word_b='птица', pos_b='noun', pos_a='adj*')
        self.assertIn('птичий', results)
        results = self.derivation.derive(word_b='лошадь', pos_b='noun', pos_a='adj*')
        self.assertIn('лошажий', results)

    def test_adj_614_2(self):
        results = self.derivation.derive(word_b='бык', pos_b='noun', pos_a='adj*')
        self.assertIn('бычачий', results)
        results = self.derivation.derive(word_b='овца', pos_b='noun', pos_a='adj*')
        self.assertIn('овечий', results)
        results = self.derivation.derive(word_b='кошка', pos_b='noun', pos_a='adj*')
        self.assertIn('кошачий', results)
        results = self.derivation.derive(word_b='русалка', pos_b='noun', pos_a='adj*')
        self.assertIn('русалочий', results)
        results = self.derivation.derive(word_b='медведь', pos_b='noun', pos_a='adj*')
        self.assertIn('медвежачий', results)
        results = self.derivation.derive(word_b='утка', pos_b='noun', pos_a='adj*')
        self.assertIn('утячий', results)
        results = self.derivation.derive(word_b='щегол', pos_b='noun', pos_a='adj*')
        self.assertIn('щеглячий', results)

    def test_adj_614_3(self):
        results = self.derivation.derive(word_b='белка', pos_b='noun', pos_a='adj*')
        self.assertIn('беличий', results)
        results = self.derivation.derive(word_b='попугай', pos_b='noun', pos_a='adj*')
        self.assertIn('попугаичий', results)

    def test_adj_614_4(self):
        results = self.derivation.derive(word_b='вол', pos_b='noun', pos_a='adj*')
        self.assertIn('воловий', results)

    def test_adj_614_5(self):
        results = self.derivation.derive(word_b='кукушка', pos_b='noun', pos_a='adj*')
        self.assertIn('кукушечий', results)
        results = self.derivation.derive(word_b='куропатка', pos_b='noun', pos_a='adj*')
        self.assertIn('куропачий', results)
        results = self.derivation.derive(word_b='жаворонок', pos_b='noun', pos_a='adj*')
        self.assertIn('жавороночий', results)

    def test_adj_614_6(self):
        results = self.derivation.derive(word_b='курица', pos_b='noun', pos_a='adj*')
        self.assertIn('куричий', results)
        self.assertIn('курячий', results)
        self.assertIn('курий', results)
        results = self.derivation.derive(word_b='свинья', pos_b='noun', pos_a='adj*')
        self.assertIn('свинячий', results)

    def test_adj_614_7(self):
        results = self.derivation.derive(word_b='кенгуру', pos_b='noun', pos_a='adj*')
        self.assertIn('кенгурий', results)

    def test_adj_614_8(self):
        results = self.derivation.derive(word_b='ребенок', pos_b='noun', pos_a='adj*')
        self.assertIn('ребячий', results)

    def test_adj_614_9(self):
        results = self.derivation.derive(word_b='гага', pos_b='noun', pos_a='adj*')
        self.assertIn('гагачий', results)

    def test_adj_614_10(self):
        results = self.derivation.derive(word_b='князь', pos_b='noun', pos_a='adj*')
        self.assertIn('княжий', results)
        results = self.derivation.derive(word_b='сёмга', pos_b='noun', pos_a='adj*')
        self.assertIn('сёмужий', results)
        results = self.derivation.derive(word_b='лебедь', pos_b='noun', pos_a='adj*')
        self.assertIn('лебяжий', results)

    def test_adj_616(self):
        results = self.derivation.derive(word_b='зверь', pos_b='noun', pos_a='adj')
        self.assertIn('звериный', results)
        results = self.derivation.derive(word_b='лев', pos_b='noun', pos_a='adj')
        self.assertIn('львиный', results)
        results = self.derivation.derive(word_b='козел', pos_b='noun', pos_a='adj')
        self.assertIn('козлиный', results)
        results = self.derivation.derive(word_b='воробей', pos_b='noun', pos_a='adj')
        self.assertIn('воробьиный', results)
        results = self.derivation.derive(word_b='змея', pos_b='noun', pos_a='adj')
        self.assertIn('змеиный', results)
        results = self.derivation.derive(word_b='утка', pos_b='noun', pos_a='adj')
        self.assertIn('утиный', results)
        results = self.derivation.derive(word_b='куры', pos_b='noun', pos_a='adj')
        self.assertIn('куриный', results)
        results = self.derivation.derive(word_b='петух', pos_b='noun', pos_a='adj')
        self.assertIn('петушиный', results)
        results = self.derivation.derive(word_b='скворец', pos_b='noun', pos_a='adj')
        self.assertIn('скворчиный', results)








if __name__ == '__main__':
    unittest.main(verbosity=2)