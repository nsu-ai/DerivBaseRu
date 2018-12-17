# -*- coding: utf-8 -*-

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

    @unittest.skip
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

    @unittest.skip
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

    @unittest.skip
    def test_adj_614_3(self):
        results = self.derivation.derive(word_b='белка', pos_b='noun', pos_a='adj*')
        self.assertIn('беличий', results)
        results = self.derivation.derive(word_b='попугай', pos_b='noun', pos_a='adj*')
        self.assertIn('попугаичий', results)

    @unittest.skip
    def test_adj_614_4(self):
        results = self.derivation.derive(word_b='вол', pos_b='noun', pos_a='adj*')
        self.assertIn('воловий', results)

    @unittest.skip
    def test_adj_614_5(self):
        results = self.derivation.derive(word_b='кукушка', pos_b='noun', pos_a='adj*')
        self.assertIn('кукушечий', results)
        results = self.derivation.derive(word_b='куропатка', pos_b='noun', pos_a='adj*')
        self.assertIn('куропачий', results)
        results = self.derivation.derive(word_b='жаворонок', pos_b='noun', pos_a='adj*')
        self.assertIn('жавороночий', results)

    @unittest.skip
    def test_adj_614_6(self):
        results = self.derivation.derive(word_b='курица', pos_b='noun', pos_a='adj*')
        self.assertIn('куричий', results)
        self.assertIn('курячий', results)
        self.assertIn('курий', results)
        results = self.derivation.derive(word_b='свинья', pos_b='noun', pos_a='adj*')
        self.assertIn('свинячий', results)

    @unittest.skip
    def test_adj_614_7(self):
        results = self.derivation.derive(word_b='кенгуру', pos_b='noun', pos_a='adj*')
        self.assertIn('кенгурий', results)

    @unittest.skip
    def test_adj_614_8(self):
        results = self.derivation.derive(word_b='ребенок', pos_b='noun', pos_a='adj*')
        self.assertIn('ребячий', results)

    @unittest.skip
    def test_adj_614_9(self):
        results = self.derivation.derive(word_b='гага', pos_b='noun', pos_a='adj*')
        self.assertIn('гагачий', results)

    @unittest.skip
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

    def test_adj_619_1(self):
        results = self.derivation.derive(word_b='одеяло', pos_b='noun', pos_a='adj')
        self.assertIn('одеяльный', results)
        results = self.derivation.derive(word_b='аренда', pos_b='noun', pos_a='adj')
        self.assertIn('арендный', results)
        results = self.derivation.derive(word_b='школа', pos_b='noun', pos_a='adj')
        self.assertIn('школьный', results)
        results = self.derivation.derive(word_b='топор', pos_b='noun', pos_a='adj')
        self.assertIn('топорный', results)
        results = self.derivation.derive(word_b='буря', pos_b='noun', pos_a='adj')
        self.assertIn('бурный', results)
        results = self.derivation.derive(word_b='неделя', pos_b='noun', pos_a='adj')
        self.assertIn('недельный', results)
        results = self.derivation.derive(word_b='уголь', pos_b='noun', pos_a='adj')
        self.assertIn('угольный', results)
        results = self.derivation.derive(word_b='футбол', pos_b='noun', pos_a='adj')
        self.assertIn('футбольный', results)
        results = self.derivation.derive(word_b='молоко', pos_b='noun', pos_a='adj')
        self.assertIn('молочный', results)
        results = self.derivation.derive(word_b='цепочка', pos_b='noun', pos_a='adj')
        self.assertIn('цепочный', results)
        results = self.derivation.derive(word_b='каторга', pos_b='noun', pos_a='adj')
        self.assertIn('каторжный', results)
        results = self.derivation.derive(word_b='долг', pos_b='noun', pos_a='adj')
        self.assertIn('должный', results)
        results = self.derivation.derive(word_b='творог', pos_b='noun', pos_a='adj')
        self.assertIn('творожный', results)
        results = self.derivation.derive(word_b='плечо', pos_b='noun', pos_a='adj')
        self.assertIn('плечной', results)
        results = self.derivation.derive(word_b='продажа', pos_b='noun', pos_a='adj')
        self.assertIn('продажный', results)
        results = self.derivation.derive(word_b='массаж', pos_b='noun', pos_a='adj')
        self.assertIn('массажный', results)
        results = self.derivation.derive(word_b='футбол', pos_b='noun', pos_a='adj')
        self.assertIn('футбольный', results)
        results = self.derivation.derive(word_b='молоко', pos_b='noun', pos_a='adj')
        self.assertIn('молочный', results)
        results = self.derivation.derive(word_b='лицо', pos_b='noun', pos_a='adj')
        self.assertIn('личный', results)
        results = self.derivation.derive(word_b='страница', pos_b='noun', pos_a='adj')
        self.assertIn('страничный', results)
        results = self.derivation.derive(word_b='огурец', pos_b='noun', pos_a='adj')
        self.assertIn('огуречный', results)
        results = self.derivation.derive(word_b='зловонье', pos_b='noun', pos_a='adj')
        self.assertIn('зловонный', results)
        results = self.derivation.derive(word_b='ружьё', pos_b='noun', pos_a='adj')
        self.assertIn('ружейный', results)
        results = self.derivation.derive(word_b='шея', pos_b='noun', pos_a='adj')
        self.assertIn('шейный', results)
        results = self.derivation.derive(word_b='бой', pos_b='noun', pos_a='adj')
        self.assertIn('бойный', results)
        results = self.derivation.derive(word_b='край', pos_b='noun', pos_a='adj')
        self.assertIn('крайний', results)
        results = self.derivation.derive(word_b='мгновение', pos_b='noun', pos_a='adj')
        self.assertIn('мгновенный', results)
        results = self.derivation.derive(word_b='сословие', pos_b='noun', pos_a='adj')
        self.assertIn('сословный', results)
        results = self.derivation.derive(word_b='лаборатория', pos_b='noun', pos_a='adj')
        self.assertIn('лабораторный', results)
        results = self.derivation.derive(word_b='инерция', pos_b='noun', pos_a='adj')
        self.assertIn('инертный', results)
        results = self.derivation.derive(word_b='сценарий', pos_b='noun', pos_a='adj')
        self.assertIn('сценарный', results)
        results = self.derivation.derive(word_b='калий', pos_b='noun', pos_a='adj')
        self.assertIn('калийный', results)
        results = self.derivation.derive(word_b='верфь', pos_b='noun', pos_a='adj')
        self.assertIn('верфный', results)
        results = self.derivation.derive(word_b='путь', pos_b='noun', pos_a='adj')
        self.assertIn('путный', results)
        results = self.derivation.derive(word_b='пламя', pos_b='noun', pos_a='adj')
        self.assertIn('пламенный', results)

    def test_adj_619_1_2(self):
        results = self.derivation.derive(word_b='гротеск', pos_b='noun', pos_a='adj')
        self.assertIn('гротескный', results)

    def test_adj_619_1_3(self):
        results = self.derivation.derive(word_b='матрац', pos_b='noun', pos_a='adj')
        self.assertIn('матрацный', results)

    @unittest.skip
    def test_adj_619_1_4(self):
        results = self.derivation.derive(word_b='факсимиле', pos_b='noun', pos_a='adj')
        self.assertIn('факсимильный', results)
        results = self.derivation.derive(word_b='барокко', pos_b='noun', pos_a='adj')
        self.assertIn('барочный', results)
        results = self.derivation.derive(word_b='соло', pos_b='noun', pos_a='adj')
        self.assertIn('сольный', results)
        results = self.derivation.derive(word_b='фортепьяно', pos_b='noun', pos_a='adj')
        self.assertIn('фортепьянный', results)

    @unittest.skip
    def test_adj_619_1_5(self):
        results = self.derivation.derive(word_b='кабаре', pos_b='noun', pos_a='adj')
        self.assertIn('кабаретный', results)
        results = self.derivation.derive(word_b='комильфо', pos_b='noun', pos_a='adj')
        self.assertIn('комильфотный', results)
        results = self.derivation.derive(word_b='буржуа', pos_b='noun', pos_a='adj')
        self.assertIn('буржуазный', results)

    @unittest.skip
    def test_adj_619_1_6(self):
        results = self.derivation.derive(word_b='дерево', pos_b='noun', pos_a='adj')
        self.assertIn('древесный', results)
        results = self.derivation.derive(word_b='слово', pos_b='noun', pos_a='adj')
        self.assertIn('словесный', results)

    @unittest.skip
    def test_adj_619_1_7(self):
        results = self.derivation.derive(word_b='яйцо', pos_b='noun', pos_a='adj')
        self.assertIn('яичный', results)

    @unittest.skip
    def test_adj_619_1_8(self):
        results = self.derivation.derive(word_b='амуниция', pos_b='noun', pos_a='adj')
        self.assertIn('амуничный', results)

    @unittest.skip
    def test_adj_619_1_9(self):
        results = self.derivation.derive(word_b='вакансия', pos_b='noun', pos_a='adj')
        self.assertIn('вакантный', results)

    def test_adj_619_1_10(self):
        results = self.derivation.derive(word_b='семья', pos_b='noun', pos_a='adj')
        self.assertIn('семейный', results)

    @unittest.skip
    def test_adj_619_1_11(self):
        results = self.derivation.derive(word_b='барахло', pos_b='noun', pos_a='adj')
        self.assertIn('барахольный', results)
        results = self.derivation.derive(word_b='игла', pos_b='noun', pos_a='adj')
        self.assertIn('игольный', results)
        results = self.derivation.derive(word_b='очки', pos_b='noun', pos_a='adj')
        self.assertIn('очёчный', results)
        results = self.derivation.derive(word_b='свёкла', pos_b='noun', pos_a='adj')
        self.assertIn('свекольный', results)
        results = self.derivation.derive(word_b='тайга', pos_b='noun', pos_a='adj')
        self.assertIn('таёжный', results)

    @unittest.skip
    def test_adj_619_1_12(self):
        results = self.derivation.derive(word_b='война', pos_b='noun', pos_a='adj')
        self.assertIn('военный', results)
        results = self.derivation.derive(word_b='корабль', pos_b='noun', pos_a='adj')
        self.assertIn('корабельный', results)
        results = self.derivation.derive(word_b='служба', pos_b='noun', pos_a='adj')
        self.assertIn('служебный', results)
        results = self.derivation.derive(word_b='польза', pos_b='noun', pos_a='adj')
        self.assertIn('полезный', results)

    @unittest.skip
    def test_adj_619_1_13(self):
        results = self.derivation.derive(word_b='дирижабль', pos_b='noun', pos_a='adj')
        self.assertIn('дирижабельный', results)
        results = self.derivation.derive(word_b='жабры', pos_b='noun', pos_a='adj')
        self.assertIn('жаберный', results)
        results = self.derivation.derive(word_b='калибр', pos_b='noun', pos_a='adj')
        self.assertIn('калиберный', results)
        results = self.derivation.derive(word_b='кегль', pos_b='noun', pos_a='adj')
        self.assertIn('кегельный', results)
        results = self.derivation.derive(word_b='солнце', pos_b='noun', pos_a='adj')
        self.assertIn('солнечный', results)
        results = self.derivation.derive(word_b='тяжба', pos_b='noun', pos_a='adj')
        self.assertIn('тяжебный', results)
        results = self.derivation.derive(word_b='легкие', pos_b='noun', pos_a='adj')
        self.assertIn('легочный', results)
        results = self.derivation.derive(word_b='насморк', pos_b='noun', pos_a='adj')
        self.assertIn('насморочный', results)
        results = self.derivation.derive(word_b='пасха', pos_b='noun', pos_a='adj')
        self.assertIn('пасочный', results)
        results = self.derivation.derive(word_b='фейерверк', pos_b='noun', pos_a='adj')
        self.assertIn('фейерверочный', results)
        results = self.derivation.derive(word_b='шеренга', pos_b='noun', pos_a='adj')
        self.assertIn('шереножный', results)

    @unittest.skip
    def test_adj_619_1_14(self):
        results = self.derivation.derive(word_b='линия', pos_b='noun', pos_a='adj')
        self.assertIn('линейный', results)
        results = self.derivation.derive(word_b='оружие', pos_b='noun', pos_a='adj')
        self.assertIn('оружейный', results)
        results = self.derivation.derive(word_b='келья', pos_b='noun', pos_a='adj')
        self.assertIn('келейный', results)
        results = self.derivation.derive(word_b='партия', pos_b='noun', pos_a='adj')
        self.assertIn('партийный', results)

    @unittest.skip
    def test_adj_619_1_15(self):
        results = self.derivation.derive(word_b='отделение', pos_b='noun', pos_a='adj')
        self.assertIn('отделённый', results)

    @unittest.skip
    def test_adj_619_1_16(self):
        results = self.derivation.derive(word_b='бунчук', pos_b='noun', pos_a='adj')
        self.assertIn('бунчужный', results)
        results = self.derivation.derive(word_b='скорняк', pos_b='noun', pos_a='adj')
        self.assertIn('скорняжный', results)
        results = self.derivation.derive(word_b='армяк', pos_b='noun', pos_a='adj')
        self.assertIn('армяжный', results)

    @unittest.skip
    def test_adj_619_1_17(self):
        results = self.derivation.derive(word_b='колодец', pos_b='noun', pos_a='adj')
        self.assertIn('колодезный', results)

    @unittest.skip
    def test_adj_619_1_18(self):
        results = self.derivation.derive(word_b='претензия', pos_b='noun', pos_a='adj')
        self.assertIn('претенциозный', results)

    @unittest.skip
    def test_adj_619_1_19(self):
        results = self.derivation.derive(word_b='земля', pos_b='noun', pos_a='adj')
        self.assertIn('земной', results)

    @unittest.skip
    def test_adj_619_1_20(self):
        results = self.derivation.derive(word_b='молоко', pos_b='noun', pos_a='adj')
        self.assertIn('млечный', results)
        results = self.derivation.derive(word_b='дерево', pos_b='noun', pos_a='adj')
        self.assertIn('древесный', results)

    @unittest.skip
    def test_adj_619_1_21(self):
        results = self.derivation.derive(word_b='бассейн', pos_b='noun', pos_a='adj')
        self.assertIn('бассейный', results)
        results = self.derivation.derive(word_b='антенна', pos_b='noun', pos_a='adj')
        self.assertIn('антенный', results)

    def test_adj_619_2(self):
        results = self.derivation.derive(word_b='язва', pos_b='noun', pos_a='adj')
        self.assertIn('язвенный', results)
        results = self.derivation.derive(word_b='манёвр', pos_b='noun', pos_a='adj')
        self.assertIn('манёвренный', results)
        results = self.derivation.derive(word_b='лекарство', pos_b='noun', pos_a='adj')
        self.assertIn('лекарственный', results)
        results = self.derivation.derive(word_b='огонь', pos_b='noun', pos_a='adj')
        self.assertIn('огненный', results)
        results = self.derivation.derive(word_b='восторг', pos_b='noun', pos_a='adj')
        self.assertIn('восторженный', results)
        results = self.derivation.derive(word_b='следствие', pos_b='noun', pos_a='adj')
        self.assertIn('следственный', results)
        results = self.derivation.derive(word_b='болезнь', pos_b='noun', pos_a='adj')
        self.assertIn('болезненный', results)

    @unittest.skip
    def test_adj_619_2_2(self):
        results = self.derivation.derive(word_b='тундра', pos_b='noun', pos_a='adj')
        self.assertIn('тундреный', results)
        results = self.derivation.derive(word_b='ветер', pos_b='noun', pos_a='adj')
        self.assertIn('ветреный', results)

    @unittest.skip
    def test_adj_619_2_3(self):
        results = self.derivation.derive(word_b='крыжовник', pos_b='noun', pos_a='adj')
        self.assertIn('крыжовенный', results)

    def test_adj_619_3(self):
        results = self.derivation.derive(word_b='индукция', pos_b='noun', pos_a='adj')
        self.assertIn('индукционный', results)
        results = self.derivation.derive(word_b='профессия', pos_b='noun', pos_a='adj')
        self.assertIn('профессиональный', results)

    def test_adj_619_4(self):
        results = self.derivation.derive(word_b='патриархат', pos_b='noun', pos_a='adj')
        self.assertIn('патриархальный', results)
        results = self.derivation.derive(word_b='уникум', pos_b='noun', pos_a='adj')
        self.assertIn('уникальный', results)
        results = self.derivation.derive(word_b='радиус', pos_b='noun', pos_a='adj')
        self.assertIn('радиальный', results)
        results = self.derivation.derive(word_b='пасха', pos_b='noun', pos_a='adj')
        self.assertIn('пасхальный', results)
        results = self.derivation.derive(word_b='федерация', pos_b='noun', pos_a='adj')
        self.assertIn('федеральный', results)
        results = self.derivation.derive(word_b='премия', pos_b='noun', pos_a='adj')
        self.assertIn('премиальный', results)
        results = self.derivation.derive(word_b='гений', pos_b='noun', pos_a='adj')
        self.assertIn('гениальный', results)

    def test_adj_619_5(self):
        results = self.derivation.derive(word_b='молекула', pos_b='noun', pos_a='adj')
        self.assertIn('молекулярный', results)
        results = self.derivation.derive(word_b='пленум', pos_b='noun', pos_a='adj')
        self.assertIn('пленарный', results)
        results = self.derivation.derive(word_b='полюс', pos_b='noun', pos_a='adj')
        self.assertIn('полярный', results)
        results = self.derivation.derive(word_b='дёготь', pos_b='noun', pos_a='adj')
        self.assertIn('дегтярный', results)

    def test_adj_619_6(self):
        results = self.derivation.derive(word_b='вена', pos_b='noun', pos_a='adj')
        self.assertIn('венозный', results)
        results = self.derivation.derive(word_b='грипп', pos_b='noun', pos_a='adj')
        self.assertIn('гриппозный', results)
        results = self.derivation.derive(word_b='скандал', pos_b='noun', pos_a='adj')
        self.assertIn('скандалёзный', results)
        results = self.derivation.derive(word_b='религия', pos_b='noun', pos_a='adj')
        self.assertIn('религиозный', results)

    @unittest.skip
    def test_adj_619_6_2(self):
        results = self.derivation.derive(word_b='экзема', pos_b='noun', pos_a='adj')
        self.assertIn('экзематозный', results)

    def test_adj_619_7(self):
        results = self.derivation.derive(word_b='рефлекс', pos_b='noun', pos_a='adj')
        self.assertIn('рефлекторный', results)
        results = self.derivation.derive(word_b='экстрасенс', pos_b='noun', pos_a='adj')
        self.assertIn('экстрасенсорный', results)
        results = self.derivation.derive(word_b='иллюзия', pos_b='noun', pos_a='adj')
        self.assertIn('иллюзорный', results)
        results = self.derivation.derive(word_b='комбинация', pos_b='noun', pos_a='adj')
        self.assertIn('комбинаторный', results)

    def test_adj_619_8(self):
        results = self.derivation.derive(word_b='текст', pos_b='noun', pos_a='adj')
        self.assertIn('текстуальный', results)
        results = self.derivation.derive(word_b='процесс', pos_b='noun', pos_a='adj')
        self.assertIn('процессуальный', results)
        results = self.derivation.derive(word_b='концепция', pos_b='noun', pos_a='adj')
        self.assertIn('концептуальный', results)

    def test_adj_619_9(self):
        results = self.derivation.derive(word_b='ультиматум', pos_b='noun', pos_a='adj')
        self.assertIn('ультимативный', results)
        results = self.derivation.derive(word_b='прогресс', pos_b='noun', pos_a='adj')
        self.assertIn('прогрессивный', results)
        results = self.derivation.derive(word_b='конверсия', pos_b='noun', pos_a='adj')
        self.assertIn('конвертивный', results)
        results = self.derivation.derive(word_b='федерация', pos_b='noun', pos_a='adj')
        self.assertIn('федеративный', results)

    @unittest.skip
    def test_adj_619_9_2(self):
        results = self.derivation.derive(word_b='консерватор', pos_b='noun', pos_a='adj')
        self.assertIn('консервативный', results)

    @unittest.skip
    def test_adj_619_9_3(self):
        results = self.derivation.derive(word_b='арго', pos_b='noun', pos_a='adj')
        self.assertIn('арготивный', results)

    def test_adj_619_10(self):
        results = self.derivation.derive(word_b='халва', pos_b='noun', pos_a='adj')
        self.assertIn('халвичный', results)
        results = self.derivation.derive(word_b='хаос', pos_b='noun', pos_a='adj')
        self.assertIn('хаотичный', results)
        results = self.derivation.derive(word_b='тип', pos_b='noun', pos_a='adj')
        self.assertIn('типичный', results)
        results = self.derivation.derive(word_b='скрипка', pos_b='noun', pos_a='adj')
        self.assertIn('скрипичный', results)
        results = self.derivation.derive(word_b='энергия', pos_b='noun', pos_a='adj')
        self.assertIn('энергичный', results)

    @unittest.skip
    def test_adj_619_10_2(self):
        results = self.derivation.derive(word_b='будни', pos_b='noun', pos_a='adj')
        self.assertIn('будничный', results)

    @unittest.skip
    def test_adj_619_10_3(self):
        results = self.derivation.derive(word_b='маслина', pos_b='noun', pos_a='adj')
        self.assertIn('масличный', results)

    @unittest.skip
    def test_adj_619_10_4(self):
        results = self.derivation.derive(word_b='драма', pos_b='noun', pos_a='adj')
        self.assertIn('драматичный', results)
        results = self.derivation.derive(word_b='симптом', pos_b='noun', pos_a='adj')
        self.assertIn('симптоматичный', results)

    @unittest.skip
    def test_adj_619_10_5(self):
        results = self.derivation.derive(word_b='гипотеза', pos_b='noun', pos_a='adj')
        self.assertIn('гипотетичный', results)

    def test_adj_619_11(self):
        results = self.derivation.derive(word_b='принцип', pos_b='noun', pos_a='adj')
        self.assertIn('принципиальный', results)
        results = self.derivation.derive(word_b='бронха', pos_b='noun', pos_a='adj')
        self.assertIn('бронхиальный', results)
        results = self.derivation.derive(word_b='провинция', pos_b='noun', pos_a='adj')
        self.assertIn('провинциальный', results)

    def test_adj_619_12(self):
        results = self.derivation.derive(word_b='образование', pos_b='noun', pos_a='adj')
        self.assertIn('образовательный', results)

    def test_adj_619_13(self):
        results = self.derivation.derive(word_b='зрение', pos_b='noun', pos_a='adj')
        self.assertIn('зрительный', results)

    @unittest.skip
    def test_adj_619_14(self):
        results = self.derivation.derive(word_b='обмолот', pos_b='noun', pos_a='adj')
        self.assertIn('обмолоточный', results)
        results = self.derivation.derive(word_b='отёлка', pos_b='noun', pos_a='adj')
        self.assertIn('отёлочный', results)
        results = self.derivation.derive(word_b='карта', pos_b='noun', pos_a='adj')
        self.assertIn('карточный', results)

    @unittest.skip
    def test_adj_619_15(self):
        results = self.derivation.derive(word_b='вина', pos_b='noun', pos_a='adj')
        self.assertIn('виновный', results)
        results = self.derivation.derive(word_b='чин', pos_b='noun', pos_a='adj')
        self.assertIn('чиновный', results)
        results = self.derivation.derive(word_b='грех', pos_b='noun', pos_a='adj')
        self.assertIn('греховный', results)
        results = self.derivation.derive(word_b='зуб', pos_b='noun', pos_a='adj')
        self.assertIn('зубовный', results)

    @unittest.skip
    def test_adj_619_16(self):
        results = self.derivation.derive(word_b='душа', pos_b='noun', pos_a='adj')
        self.assertIn('душевный', results)
        results = self.derivation.derive(word_b='плач', pos_b='noun', pos_a='adj')
        self.assertIn('плачевный', results)
        results = self.derivation.derive(word_b='день', pos_b='noun', pos_a='adj')
        self.assertIn('дневной', results)

    @unittest.skip
    def test_adj_619_17(self):
        results = self.derivation.derive(word_b='враг', pos_b='noun', pos_a='adj')
        self.assertIn('враждебный', results)
        results = self.derivation.derive(word_b='суд', pos_b='noun', pos_a='adj')
        self.assertIn('судебный', results)
        results = self.derivation.derive(word_b='врач', pos_b='noun', pos_a='adj')
        self.assertIn('врачебный', results)

    @unittest.skip
    def test_adj_619_18(self):
        results = self.derivation.derive(word_b='желе', pos_b='noun', pos_a='adj')
        self.assertIn('желейный', results)
        results = self.derivation.derive(word_b='жалюзи', pos_b='noun', pos_a='adj')
        self.assertIn('жалюзийный', results)
        results = self.derivation.derive(word_b='кино', pos_b='noun', pos_a='adj')
        self.assertIn('киношный', results)
        results = self.derivation.derive(word_b='фэзэу', pos_b='noun', pos_a='adj')
        self.assertIn('фэзэушный', results)

    @unittest.skip
    def test_adj_619_18_2(self):
        results = self.derivation.derive(word_b='алоэ', pos_b='noun', pos_a='adj')
        self.assertIn('алойный', results)

    def test_adj_619_19(self):
        results = self.derivation.derive(word_b='ум', pos_b='noun', pos_a='adj')
        self.assertIn('умственный', results)
        results = self.derivation.derive(word_b='женщина', pos_b='noun', pos_a='adj')
        self.assertIn('женственный', results)
        results = self.derivation.derive(word_b='насилие', pos_b='noun', pos_a='adj')
        self.assertIn('насильственный', results)

    @unittest.skip
    def test_adj_619_20(self):
        results = self.derivation.derive(word_b='солод', pos_b='noun', pos_a='adj')
        self.assertIn('солодовенный', results)

    @unittest.skip
    def test_adj_619_21(self):
        results = self.derivation.derive(word_b='смерть', pos_b='noun', pos_a='adj')
        self.assertIn('смертельный', results)
        results = self.derivation.derive(word_b='платье', pos_b='noun', pos_a='adj')
        self.assertIn('плательный', results)

    @unittest.skip
    def test_adj_619_22(self):
        results = self.derivation.derive(word_b='гвоздь', pos_b='noun', pos_a='adj')
        self.assertIn('гвоздильный', results)

    @unittest.skip
    def test_adj_619_23(self):
        results = self.derivation.derive(word_b='геморрой', pos_b='noun', pos_a='adj')
        self.assertIn('геморроидальный', results)
        results = self.derivation.derive(word_b='трапеция', pos_b='noun', pos_a='adj')
        self.assertIn('трапецеидальный', results)

    @unittest.skip
    def test_adj_619_24(self):
        results = self.derivation.derive(word_b='скерцо', pos_b='noun', pos_a='adj')
        self.assertIn('скерциозный', results)
        results = self.derivation.derive(word_b='претензия', pos_b='noun', pos_a='adj')
        self.assertIn('претенциозный', results)

    @unittest.skip
    def test_adj_619_25(self):
        results = self.derivation.derive(word_b='помпа', pos_b='noun', pos_a='adj')
        self.assertIn('помпезный', results)

    @unittest.skip
    def test_adj_619_26(self):
        results = self.derivation.derive(word_b='цинга', pos_b='noun', pos_a='adj')
        self.assertIn('цинготный', results)
        results = self.derivation.derive(word_b='кроха', pos_b='noun', pos_a='adj')
        self.assertIn('крохотный', results)

    @unittest.skip
    def test_adj_619_27(self):
        results = self.derivation.derive(word_b='телевидение', pos_b='noun', pos_a='adj')
        self.assertIn('телевизионный', results)

    @unittest.skip
    def test_adj_619_28(self):
        results = self.derivation.derive(word_b='экзамен', pos_b='noun', pos_a='adj')
        self.assertIn('экзаменационный', results)

    @unittest.skip
    def test_adj_619_29(self):
        results = self.derivation.derive(word_b='портной', pos_b='noun', pos_a='adj')
        self.assertIn('портняжный', results)

    def test_adj_623(self):
        results = self.derivation.derive(word_b='супруг', pos_b='noun', pos_a='adj')
        self.assertIn('супружний', results)
        results = self.derivation.derive(word_b='матерь', pos_b='noun', pos_a='adj')
        self.assertIn('матерний', results)
        results = self.derivation.derive(word_b='сын', pos_b='noun', pos_a='adj')
        self.assertIn('сыновний', results)
        results = self.derivation.derive(word_b='перед', pos_b='noun', pos_a='adj')
        self.assertIn('передний', results)
        results = self.derivation.derive(word_b='верх', pos_b='noun', pos_a='adj')
        self.assertIn('верхний', results)
        results = self.derivation.derive(word_b='низ', pos_b='noun', pos_a='adj')
        self.assertIn('нижний', results)
        results = self.derivation.derive(word_b='край', pos_b='noun', pos_a='adj')
        self.assertIn('крайний', results)
        results = self.derivation.derive(word_b='сторона', pos_b='noun', pos_a='adj')
        self.assertIn('сторонний', results)
        results = self.derivation.derive(word_b='лето', pos_b='noun', pos_a='adj')
        self.assertIn('летний', results)
        results = self.derivation.derive(word_b='весна', pos_b='noun', pos_a='adj')
        self.assertIn('весенний', results)
        results = self.derivation.derive(word_b='утро', pos_b='noun', pos_a='adj')
        self.assertIn('утренний', results)
        results = self.derivation.derive(word_b='утро', pos_b='noun', pos_a='adj')
        self.assertIn('утрешний', results)
        results = self.derivation.derive(word_b='будни', pos_b='noun', pos_a='adj')
        self.assertIn('буднишний', results)
        results = self.derivation.derive(word_b='правда', pos_b='noun', pos_a='adj')
        self.assertIn('правдашний', results)

    def test_adj_624(self):
        results = self.derivation.derive(word_b='береста', pos_b='noun', pos_a='adj')
        self.assertIn('берестяной', results)
        results = self.derivation.derive(word_b='волос', pos_b='noun', pos_a='adj')
        self.assertIn('волосяной', results)
        results = self.derivation.derive(word_b='ветер', pos_b='noun', pos_a='adj')
        self.assertIn('ветряный', results)
        results = self.derivation.derive(word_b='дупло', pos_b='noun', pos_a='adj')
        self.assertIn('дупляной', results)
        results = self.derivation.derive(word_b='гвоздь', pos_b='noun', pos_a='adj')
        self.assertIn('гвоздяной', results)
        results = self.derivation.derive(word_b='кожа', pos_b='noun', pos_a='adj')
        self.assertIn('кожаный', results)
        results = self.derivation.derive(word_b='ветвь', pos_b='noun', pos_a='adj')
        self.assertIn('ветвяной', results)
        results = self.derivation.derive(word_b='таволги', pos_b='noun', pos_a='adj')
        self.assertIn('таволжаный', results)
        results = self.derivation.derive(word_b='мох', pos_b='noun', pos_a='adj')
        self.assertIn('мшаный', results)
        results = self.derivation.derive(word_b='воск', pos_b='noun', pos_a='adj')
        self.assertIn('вощаной', results)
        results = self.derivation.derive(word_b='лёд', pos_b='noun', pos_a='adj')
        self.assertIn('ледяной', results)
        results = self.derivation.derive(word_b='платье', pos_b='noun', pos_a='adj')
        self.assertIn('платяной', results)
        results = self.derivation.derive(word_b='хлопья', pos_b='noun', pos_a='adj')
        self.assertIn('хлопяной', results)
        results = self.derivation.derive(word_b='мёд', pos_b='noun', pos_a='adj')
        self.assertIn('медвяный', results)
        results = self.derivation.derive(word_b='дух', pos_b='noun', pos_a='adj')
        self.assertIn('духмяный', results)
        results = self.derivation.derive(word_b='тростник', pos_b='noun', pos_a='adj')
        self.assertIn('тростяной', results)

    def test_adj_625(self):
        results = self.derivation.derive(word_b='стекло', pos_b='noun', pos_a='adj')
        self.assertIn('стеклянный', results)

    def test_adj_626(self):
        results = self.derivation.derive(word_b='рента', pos_b='noun', pos_a='adj')
        self.assertIn('рентабельный', results)
        results = self.derivation.derive(word_b='комфорт', pos_b='noun', pos_a='adj')
        self.assertIn('комфортабельный', results)
        results = self.derivation.derive(word_b='коммуникация', pos_b='noun', pos_a='adj')
        self.assertIn('коммуникабельный', results)

    def test_adj_627(self):
        results = self.derivation.derive(word_b='купе', pos_b='noun', pos_a='adj')
        self.assertIn('купированный', results)
        results = self.derivation.derive(word_b='квалификация', pos_b='noun', pos_a='adj')
        self.assertIn('квалифицированный', results)
        results = self.derivation.derive(word_b='привилегия', pos_b='noun', pos_a='adj')
        self.assertIn('привилегированный', results)
        results = self.derivation.derive(word_b='экзальтация', pos_b='noun', pos_a='adj')
        self.assertIn('экзальтированный', results)
        results = self.derivation.derive(word_b='эрудиция', pos_b='noun', pos_a='adj')
        self.assertIn('эрудированный', results)

    def test_adj_628(self):
        results = self.derivation.derive(word_b='тундра', pos_b='noun', pos_a='adj')
        self.assertIn('тундровый', results)
        results = self.derivation.derive(word_b='дом', pos_b='noun', pos_a='adj')
        self.assertIn('домовый', results)
        results = self.derivation.derive(word_b='одеяло', pos_b='noun', pos_a='adj')
        self.assertIn('одеяловый', results)
        results = self.derivation.derive(word_b='вишня', pos_b='noun', pos_a='adj')
        self.assertIn('вишнёвый', results)
        results = self.derivation.derive(word_b='соболь', pos_b='noun', pos_a='adj')
        self.assertIn('соболевый', results)
        results = self.derivation.derive(word_b='поле', pos_b='noun', pos_a='adj')
        self.assertIn('полевой', results)
        results = self.derivation.derive(word_b='грядка', pos_b='noun', pos_a='adj')
        self.assertIn('грядковый', results)
        results = self.derivation.derive(word_b='берег', pos_b='noun', pos_a='adj')
        self.assertIn('береговой', results)
        results = self.derivation.derive(word_b='стрелок', pos_b='noun', pos_a='adj')
        self.assertIn('стрелковый', results)
        results = self.derivation.derive(word_b='замша', pos_b='noun', pos_a='adj')
        self.assertIn('замшевый', results)
        results = self.derivation.derive(word_b='морж', pos_b='noun', pos_a='adj')
        self.assertIn('моржовый', results)
        results = self.derivation.derive(word_b='синица', pos_b='noun', pos_a='adj')
        self.assertIn('синицевый', results)
        results = self.derivation.derive(word_b='ситец', pos_b='noun', pos_a='adj')
        self.assertIn('ситцевый', results)
        results = self.derivation.derive(word_b='лицо', pos_b='noun', pos_a='adj')
        self.assertIn('лицевой', results)
        results = self.derivation.derive(word_b='горностай', pos_b='noun', pos_a='adj')
        self.assertIn('горностаевый', results)
        results = self.derivation.derive(word_b='сырьё', pos_b='noun', pos_a='adj')
        self.assertIn('сырьевой', results)
        results = self.derivation.derive(word_b='боль', pos_b='noun', pos_a='adj')
        self.assertIn('болевой', results)
        results = self.derivation.derive(word_b='путь', pos_b='noun', pos_a='adj')
        self.assertIn('путевой', results)

    def test_adj_628_2(self):
        results = self.derivation.derive(word_b='звено', pos_b='noun', pos_a='adj')
        self.assertIn('звеньевой', results)
        results = self.derivation.derive(word_b='перо', pos_b='noun', pos_a='adj')
        self.assertIn('перьевой', results)
        results = self.derivation.derive(word_b='судно', pos_b='noun', pos_a='adj')
        self.assertIn('судовой', results)

    def test_adj_628_3(self):
        results = self.derivation.derive(word_b='кенгуру', pos_b='noun', pos_a='adj')
        self.assertIn('кенгуровый', results)
        results = self.derivation.derive(word_b='джерси', pos_b='noun', pos_a='adj')
        self.assertIn('джерсевый', results)
        results = self.derivation.derive(word_b='джерсе', pos_b='noun', pos_a='adj')
        self.assertIn('джерсовый', results)
        results = self.derivation.derive(word_b='такси', pos_b='noun', pos_a='adj')
        self.assertIn('таксовый', results)

    def test_adj_628_4(self):
        results = self.derivation.derive(word_b='можжевельник', pos_b='noun', pos_a='adj')
        self.assertIn('можжевёловый', results)

    def test_adj_628_5(self):
        results = self.derivation.derive(word_b='клеть', pos_b='noun', pos_a='adj')
        self.assertIn('клетьевой', results)
        results = self.derivation.derive(word_b='глубь', pos_b='noun', pos_a='adj')
        self.assertIn('глубьевой', results)
        results = self.derivation.derive(word_b='герань', pos_b='noun', pos_a='adj')
        self.assertIn('гераниевый', results)

    def test_adj_628_6(self):
        results = self.derivation.derive(word_b='греча', pos_b='noun', pos_a='adj')
        self.assertIn('гречневый', results)

    def test_adj_628_7(self):
        results = self.derivation.derive(word_b='кора', pos_b='noun', pos_a='adj')
        self.assertIn('корковый', results)
        results = self.derivation.derive(word_b='ячмень', pos_b='noun', pos_a='adj')
        self.assertIn('ячневый', results)

    def test_adj_628_8(self):
        results = self.derivation.derive(word_b='какао', pos_b='noun', pos_a='adj')
        self.assertIn('какаовый', results)

    def test_adj_628_9(self):
        results = self.derivation.derive(word_b='жёрнов', pos_b='noun', pos_a='adj')
        self.assertIn('жерновой', results)
        results = self.derivation.derive(word_b='бечева', pos_b='noun', pos_a='adj')
        self.assertIn('бечевой', results)
        results = self.derivation.derive(word_b='швартов', pos_b='noun', pos_a='adj')
        self.assertIn('швартовый', results)

    def test_adj_628_10(self):
        results = self.derivation.derive(word_b='узел', pos_b='noun', pos_a='adj')
        self.assertIn('узловой', results)
        results = self.derivation.derive(word_b='сосна', pos_b='noun', pos_a='adj')
        self.assertIn('сосновый', results)

    def test_adj_628_11(self):
        results = self.derivation.derive(word_b='лёд', pos_b='noun', pos_a='adj')
        self.assertIn('ледовый', results)
        results = self.derivation.derive(word_b='лоб', pos_b='noun', pos_a='adj')
        self.assertIn('лобовой', results)

    def test_adj_628_12(self):
        results = self.derivation.derive(word_b='рана', pos_b='noun', pos_a='adj')
        self.assertIn('раневой', results)
        results = self.derivation.derive(word_b='смола', pos_b='noun', pos_a='adj')
        self.assertIn('смолевой', results)
        results = self.derivation.derive(word_b='смола', pos_b='noun', pos_a='adj')
        self.assertIn('смолёвый', results)
        results = self.derivation.derive(word_b='плюсна', pos_b='noun', pos_a='adj')
        self.assertIn('плюсневой', results)
        results = self.derivation.derive(word_b='гол', pos_b='noun', pos_a='adj')
        self.assertIn('голевой', results)
        results = self.derivation.derive(word_b='зверь', pos_b='noun', pos_a='adj')
        self.assertIn('зверовой', results)
        results = self.derivation.derive(word_b='дробь', pos_b='noun', pos_a='adj')
        self.assertIn('дробовой', results)
        results = self.derivation.derive(word_b='ель', pos_b='noun', pos_a='adj')
        self.assertIn('еловый', results)
        results = self.derivation.derive(word_b='весть', pos_b='noun', pos_a='adj')
        self.assertIn('вестовой', results)
        results = self.derivation.derive(word_b='жёлудь', pos_b='noun', pos_a='adj')
        self.assertIn('желудовый', results)

    def test_adj_628_13(self):
        results = self.derivation.derive(word_b='холст', pos_b='noun', pos_a='adj')
        self.assertIn('холщевый', results)
        results = self.derivation.derive(word_b='зябь', pos_b='noun', pos_a='adj')
        self.assertIn('зяблевый', results)

    def test_adj_631_1(self):
        results = self.derivation.derive(word_b='Одесса', pos_b='noun', pos_a='adj')
        self.assertIn('одесский', results)
        results = self.derivation.derive(word_b='сосед', pos_b='noun', pos_a='adj')
        self.assertIn('соседский', results)
        results = self.derivation.derive(word_b='арсенал', pos_b='noun', pos_a='adj')
        self.assertIn('арсенальский', results)
        results = self.derivation.derive(word_b='февраль', pos_b='noun', pos_a='adj')
        self.assertIn('февральский', results)
        results = self.derivation.derive(word_b='конь', pos_b='noun', pos_a='adj')
        self.assertIn('конский', results)
        results = self.derivation.derive(word_b='Сумы', pos_b='noun', pos_a='adj')
        self.assertIn('сумский', results)
        results = self.derivation.derive(word_b='море', pos_b='noun', pos_a='adj')
        self.assertIn('морской', results)
        results = self.derivation.derive(word_b='чех', pos_b='noun', pos_a='adj')
        self.assertIn('чешский', results)
        results = self.derivation.derive(word_b='казак', pos_b='noun', pos_a='adj')
        self.assertIn('казацкий', results)
        results = self.derivation.derive(word_b='Париж', pos_b='noun', pos_a='adj')
        self.assertIn('парижский', results)
        results = self.derivation.derive(word_b='Винница', pos_b='noun', pos_a='adj')
        self.assertIn('винницкий', results)
        results = self.derivation.derive(word_b='немец', pos_b='noun', pos_a='adj')
        self.assertIn('немецкий', results)
        results = self.derivation.derive(word_b='май', pos_b='noun', pos_a='adj')
        self.assertIn('майский', results)
        results = self.derivation.derive(word_b='Мордовия', pos_b='noun', pos_a='adj')
        self.assertIn('мордовский', results)
        results = self.derivation.derive(word_b='Англия', pos_b='noun', pos_a='adj')
        self.assertIn('английский', results)
        results = self.derivation.derive(word_b='Бразилия', pos_b='noun', pos_a='adj')
        self.assertIn('бразильский', results)
        results = self.derivation.derive(word_b='Пермь', pos_b='noun', pos_a='adj')
        self.assertIn('пермский', results)

    def test_adj_631_1_2(self):
        results = self.derivation.derive(word_b='Моздок', pos_b='noun', pos_a='adj')
        self.assertIn('моздокский', results)
        results = self.derivation.derive(word_b='Лейпциг', pos_b='noun', pos_a='adj')
        self.assertIn('лейпцигский', results)
        results = self.derivation.derive(word_b='Палех', pos_b='noun', pos_a='adj')
        self.assertIn('палехский', results)
        results = self.derivation.derive(word_b='нивхи', pos_b='noun', pos_a='adj')
        self.assertIn('нивхский', results)

    def test_adj_631_1_3(self):
        results = self.derivation.derive(word_b='герцог', pos_b='noun', pos_a='adj')
        self.assertIn('герцогский', results)
        results = self.derivation.derive(word_b='шах', pos_b='noun', pos_a='adj')
        self.assertIn('шахский', results)

    def test_adj_631_1_4(self):
        results = self.derivation.derive(word_b='сентябрь', pos_b='noun', pos_a='adj')
        self.assertIn('сентябрьский', results)
        results = self.derivation.derive(word_b='июнь', pos_b='noun', pos_a='adj')
        self.assertIn('июньский', results)
        results = self.derivation.derive(word_b='день', pos_b='noun', pos_a='adj')
        self.assertIn('деньской', results)

    def test_adj_631_1_5(self):
        results = self.derivation.derive(word_b='Ямал', pos_b='noun', pos_a='adj')
        self.assertIn('ямалский', results)
        results = self.derivation.derive(word_b='Пномпень', pos_b='noun', pos_a='adj')
        self.assertIn('пномпеньский', results)

    def test_adj_631_1_6(self):
        results = self.derivation.derive(word_b='Бордо', pos_b='noun', pos_a='adj')
        self.assertIn('бордоский', results)
        results = self.derivation.derive(word_b='Ватерлоо', pos_b='noun', pos_a='adj')
        self.assertIn('ватерлооский', results)
        results = self.derivation.derive(word_b='майя', pos_b='noun', pos_a='adj')
        self.assertIn('майяский', results)
        results = self.derivation.derive(word_b='Тарту', pos_b='noun', pos_a='adj')
        self.assertIn('тартуский', results)
        results = self.derivation.derive(word_b='Раквере', pos_b='noun', pos_a='adj')
        self.assertIn('раквереский', results)
        results = self.derivation.derive(word_b='Чарджоу', pos_b='noun', pos_a='adj')
        self.assertIn('чарджоуский', results)

    def test_adj_631_2(self):
        results = self.derivation.derive(word_b='ребята', pos_b='noun', pos_a='adj')
        self.assertIn('ребяческий', results)
        results = self.derivation.derive(word_b='князь', pos_b='noun', pos_a='adj')
        self.assertIn('княжеский', results)
        results = self.derivation.derive(word_b='логика', pos_b='noun', pos_a='adj')
        self.assertIn('логический', results)
        results = self.derivation.derive(word_b='друг', pos_b='noun', pos_a='adj')
        self.assertIn('дружеский', results)
        results = self.derivation.derive(word_b='ханжа', pos_b='noun', pos_a='adj')
        self.assertIn('ханжеский', results)
        results = self.derivation.derive(word_b='трюкач', pos_b='noun', pos_a='adj')
        self.assertIn('трюкаческий', results)
        results = self.derivation.derive(word_b='купец', pos_b='noun', pos_a='adj')
        self.assertIn('купеческий', results)

    def test_adj_631_2_2(self):
        results = self.derivation.derive(word_b='князь', pos_b='noun', pos_a='adj')
        self.assertIn('княжеский', results)

    def test_adj_631_3(self):
        results = self.derivation.derive(word_b='Массандра', pos_b='noun', pos_a='adj')
        self.assertIn('массандровский', results)
        results = self.derivation.derive(word_b='вор', pos_b='noun', pos_a='adj')
        self.assertIn('воровской', results)
        results = self.derivation.derive(word_b='кремль', pos_b='noun', pos_a='adj')
        self.assertIn('кремлевский', results)
        results = self.derivation.derive(word_b='жених', pos_b='noun', pos_a='adj')
        self.assertIn('жениховский', results)
        results = self.derivation.derive(word_b='фриц', pos_b='noun', pos_a='adj')
        self.assertIn('фрицевский', results)
        results = self.derivation.derive(word_b='отец', pos_b='noun', pos_a='adj')
        self.assertIn('отцовский', results)

    def test_adj_631_3_2(self):
        results = self.derivation.derive(word_b='Горький', pos_b='noun_adj', pos_a='adj')
        self.assertIn('горьковский', results)
        results = self.derivation.derive(word_b='Гойя', pos_b='noun', pos_a='adj')
        self.assertIn('гойевский', results)
        results = self.derivation.derive(word_b='ЖюльВерн', pos_b='noun', pos_a='adj')
        self.assertIn('жюльверновский', results)

    def test_adj_631_3_3(self):
        results = self.derivation.derive(word_b='Клинцы', pos_b='noun', pos_a='adj')
        self.assertIn('клинцовский', results)
        results = self.derivation.derive(word_b='Нагорье', pos_b='noun', pos_a='adj')
        self.assertIn('нагорьевский', results)

    def test_adj_632_1(self):
        results = self.derivation.derive(word_b='Америка', pos_b='noun', pos_a='adj')
        self.assertIn('американский', results)
        results = self.derivation.derive(word_b='Бирма', pos_b='noun', pos_a='adj')
        self.assertIn('бирманский', results)
        results = self.derivation.derive(word_b='Рудня', pos_b='noun', pos_a='adj')
        self.assertIn('руднянский', results)
        results = self.derivation.derive(word_b='Орша', pos_b='noun', pos_a='adj')
        self.assertIn('оршанский', results)
        results = self.derivation.derive(word_b='Венеция', pos_b='noun', pos_a='adj')
        self.assertIn('венецианский', results)
        results = self.derivation.derive(word_b='Россошь', pos_b='noun', pos_a='adj')
        self.assertIn('россошанский', results)

    def test_adj_632_1_2(self):
        results = self.derivation.derive(word_b='Перу', pos_b='noun', pos_a='adj')
        self.assertIn('перуанский', results)

    def test_adj_632_2(self):
        results = self.derivation.derive(word_b='Чита', pos_b='noun', pos_a='adj')
        self.assertIn('читинский', results)
        results = self.derivation.derive(word_b='Лодзь', pos_b='noun', pos_a='adj')
        self.assertIn('лодзинский', results)
        results = self.derivation.derive(word_b='Шахты', pos_b='noun', pos_a='adj')
        self.assertIn('шахтинский', results)
        results = self.derivation.derive(word_b='Мирный', pos_b='noun', pos_a='adj')
        self.assertIn('мирнинский', results)
        results = self.derivation.derive(word_b='Мытыщи', pos_b='noun', pos_a='adj')
        self.assertIn('мытищинский', results)
        results = self.derivation.derive(word_b='Пенза', pos_b='noun', pos_a='adj')
        self.assertIn('пензенский', results)
        results = self.derivation.derive(word_b='Керчь', pos_b='noun', pos_a='adj')
        self.assertIn('керченский', results)
        results = self.derivation.derive(word_b='городище', pos_b='noun', pos_a='adj')
        self.assertIn('городищенский', results)
        results = self.derivation.derive(word_b='Екатерина', pos_b='noun', pos_a='adj')
        self.assertIn('екатерининский', results)
        results = self.derivation.derive(word_b='матерь', pos_b='noun', pos_a='adj')
        self.assertIn('материнский', results)
        results = self.derivation.derive(word_b='сатана', pos_b='noun', pos_a='adj')
        self.assertIn('сатанинский', results)
        results = self.derivation.derive(word_b='нищий', pos_b='noun_adj', pos_a='adj')
        self.assertIn('нищенский', results)
        results = self.derivation.derive(word_b='кладбище', pos_b='noun', pos_a='adj')
        self.assertIn('кладбищенский', results)
        results = self.derivation.derive(word_b='рождество', pos_b='noun', pos_a='adj')
        self.assertIn('рождественский', results)
        results = self.derivation.derive(word_b='Фрунзе', pos_b='noun', pos_a='adj')
        self.assertIn('фрунзенский', results)
        results = self.derivation.derive(word_b='Известия', pos_b='noun', pos_a='adj')
        self.assertIn('известинский', results)

    def test_adj_632_3(self):
        results = self.derivation.derive(word_b='эвенки', pos_b='noun', pos_a='adj')
        self.assertIn('эвенкийский', results)
        results = self.derivation.derive(word_b='Альпы', pos_b='noun', pos_a='adj')
        self.assertIn('альпийский', results)
        results = self.derivation.derive(word_b='Уганда', pos_b='noun', pos_a='adj')
        self.assertIn('угандийский', results)
        results = self.derivation.derive(word_b='Олимп', pos_b='noun', pos_a='adj')
        self.assertIn('олимпийский', results)

    def test_adj_632_4(self):
        results = self.derivation.derive(word_b='сцена', pos_b='noun', pos_a='adj')
        self.assertIn('сценический', results)
        results = self.derivation.derive(word_b='алгебра', pos_b='noun', pos_a='adj')
        self.assertIn('алгебраический', results)
        results = self.derivation.derive(word_b='эпизод', pos_b='noun', pos_a='adj')
        self.assertIn('эпизодический', results)
        results = self.derivation.derive(word_b='идеолог', pos_b='noun', pos_a='adj')
        self.assertIn('идеологический', results)
        results = self.derivation.derive(word_b='герой', pos_b='noun', pos_a='adj')
        self.assertIn('героический', results)
        results = self.derivation.derive(word_b='верноподданный', pos_b='noun_adj', pos_a='adj')
        self.assertIn('верноподданнический', results)

    def test_adj_632_5(self):
        results = self.derivation.derive(word_b='краевед', pos_b='noun', pos_a='adj')
        self.assertIn('краеведческий', results)
        results = self.derivation.derive(word_b='винодел', pos_b='noun', pos_a='adj')
        self.assertIn('винодельческий', results)
        results = self.derivation.derive(word_b='учреждение', pos_b='noun', pos_a='adj')
        self.assertIn('учрежденческий', results)

    def test_adj_632_6(self):
        results = self.derivation.derive(word_b='ханты', pos_b='noun', pos_a='adj')
        self.assertIn('хантыйский', results)
        results = self.derivation.derive(word_b='Чу', pos_b='noun', pos_a='adj')
        self.assertIn('чуйский', results)
        results = self.derivation.derive(word_b='Хуло', pos_b='noun', pos_a='adj')
        self.assertIn('хулойский', results)

    def test_adj_632_7(self):
        results = self.derivation.derive(word_b='Улан-Удэ', pos_b='noun', pos_a='adj')
        self.assertIn('улан-удэнский', results)
        results = self.derivation.derive(word_b='эрзя', pos_b='noun', pos_a='adj')
        self.assertIn('эрзянский', results)

    def test_adj_632_8(self):
        results = self.derivation.derive(word_b='Ришелье', pos_b='noun', pos_a='adj')
        self.assertIn('ришельевский', results)

    def test_adj_632_9(self):
        results = self.derivation.derive(word_b='Верди', pos_b='noun', pos_a='adj')
        self.assertIn('вердиевский', results)

    def test_adj_632_10(self):
        results = self.derivation.derive(word_b='Венера', pos_b='noun', pos_a='adj')
        self.assertIn('венерианский', results)
        results = self.derivation.derive(word_b='Меркурий', pos_b='noun', pos_a='adj')
        self.assertIn('меркурианский', results)

    def test_adj_632_11(self):
        results = self.derivation.derive(word_b='путь', pos_b='noun', pos_a='adj')
        self.assertIn('путейский', results)
        results = self.derivation.derive(word_b='Европа', pos_b='noun', pos_a='adj')
        self.assertIn('европейский', results)

    def test_adj_632_12(self):
        results = self.derivation.derive(word_b='Генуя', pos_b='noun', pos_a='adj')
        self.assertIn('генуэзский', results)
        results = self.derivation.derive(word_b='Ангола', pos_b='noun', pos_a='adj')
        self.assertIn('анголезский', results)
        results = self.derivation.derive(word_b='Конго', pos_b='noun', pos_a='adj')
        self.assertIn('конголезский', results)
        results = self.derivation.derive(word_b='Того', pos_b='noun', pos_a='adj')
        self.assertIn('тоголезский', results)

    def test_adj_632_13(self):
        results = self.derivation.derive(word_b='король', pos_b='noun', pos_a='adj')
        self.assertIn('королевский', results)

    def test_adj_632_14(self):
        results = self.derivation.derive(word_b='Брно', pos_b='noun', pos_a='adj')
        self.assertIn('брненский', results)

    def test_adj_632_15(self):
        results = self.derivation.derive(word_b='Уфа', pos_b='noun', pos_a='adj')
        self.assertIn('уфимский', results)

    def test_adj_632_16(self):
        results = self.derivation.derive(word_b='Выкса', pos_b='noun', pos_a='adj')
        self.assertIn('выксунский', results)

    def test_adj_632_17(self):
        results = self.derivation.derive(word_b='табу', pos_b='noun', pos_a='adj')
        self.assertIn('табуистический', results)

    def test_adj_632_18(self):
        results = self.derivation.derive(word_b='хохол', pos_b='noun', pos_a='adj')
        self.assertIn('хохлацкий', results)

    def test_adj_632_19(self):
        results = self.derivation.derive(word_b='Чикаго', pos_b='noun', pos_a='adj')
        self.assertIn('чикагский', results)
        results = self.derivation.derive(word_b='Миссисипи', pos_b='noun', pos_a='adj')
        self.assertIn('миссисипский', results)
        results = self.derivation.derive(word_b='саами', pos_b='noun', pos_a='adj')
        self.assertIn('саамский', results)
        results = self.derivation.derive(word_b='Урарту', pos_b='noun', pos_a='adj')
        self.assertIn('урартский', results)
        results = self.derivation.derive(word_b='Кошице', pos_b='noun', pos_a='adj')
        self.assertIn('кошицкий', results)
        results = self.derivation.derive(word_b='Кони', pos_b='noun', pos_a='adj')
        self.assertIn('коневский', results)
        results = self.derivation.derive(word_b='Цхакая', pos_b='noun', pos_a='adj')
        self.assertIn('цхакаевский', results)
        results = self.derivation.derive(word_b='Фрунзе', pos_b='noun', pos_a='adj')
        self.assertIn('фрунзенский', results)
        results = self.derivation.derive(word_b='Туапсе', pos_b='noun', pos_a='adj')
        self.assertIn('туапсинский', results)
        results = self.derivation.derive(word_b='Баку', pos_b='noun', pos_a='adj')
        self.assertIn('бакинский', results)
        results = self.derivation.derive(word_b='Сорренто', pos_b='noun', pos_a='adj')
        self.assertIn('соррентийский', results)

    def test_adj_632_20(self):
        results = self.derivation.derive(word_b='крещение', pos_b='noun', pos_a='adj')
        self.assertIn('крещенский', results)
        results = self.derivation.derive(word_b='поведение', pos_b='noun', pos_a='adj')
        self.assertIn('поведенческий', results)
        results = self.derivation.derive(word_b='канцелярия', pos_b='noun', pos_a='adj')
        self.assertIn('канцелярский', results)
        results = self.derivation.derive(word_b='гимназия', pos_b='noun', pos_a='adj')
        self.assertIn('гимназический', results)
        results = self.derivation.derive(word_b='Кахетия', pos_b='noun', pos_a='adj')
        self.assertIn('кахетинский', results)
        results = self.derivation.derive(word_b='пролетарий', pos_b='noun', pos_a='adj')
        self.assertIn('пролетарский', results)
        results = self.derivation.derive(word_b='евангелие', pos_b='noun', pos_a='adj')
        self.assertIn('евангельский', results)
        results = self.derivation.derive(word_b='амфибрахий', pos_b='noun', pos_a='adj')
        self.assertIn('амфибрахический', results)
        results = self.derivation.derive(word_b='Болонья', pos_b='noun', pos_a='adj')
        self.assertIn('болонский', results)
        results = self.derivation.derive(word_b='Севилья', pos_b='noun', pos_a='adj')
        self.assertIn('севильский', results)
        results = self.derivation.derive(word_b='Усолье', pos_b='noun', pos_a='adj')
        self.assertIn('усольский', results)
        results = self.derivation.derive(word_b='Щучье', pos_b='noun', pos_a='adj')
        self.assertIn('щучинский', results)
        results = self.derivation.derive(word_b='Заречье', pos_b='noun', pos_a='adj')
        self.assertIn('зареченский', results)
        results = self.derivation.derive(word_b='патриций', pos_b='noun', pos_a='adj')
        self.assertIn('патрицианский', results)

    def test_adj_632_21(self):
        results = self.derivation.derive(word_b='беженец', pos_b='noun', pos_a='adj')
        self.assertIn('беженский', results)
        results = self.derivation.derive(word_b='якобинец', pos_b='noun', pos_a='adj')
        self.assertIn('якобинский', results)
        results = self.derivation.derive(word_b='нанаец', pos_b='noun', pos_a='adj')
        self.assertIn('нанайский', results)

    def test_adj_632_22(self):
        results = self.derivation.derive(word_b='Дамаск', pos_b='noun', pos_a='adj')
        self.assertIn('дамасский', results)
        results = self.derivation.derive(word_b='этруски', pos_b='noun', pos_a='adj')
        self.assertIn('этрусский', results)
        results = self.derivation.derive(word_b='Сан-Франциско', pos_b='noun', pos_a='adj')
        self.assertIn('сан-францисский', results)

    def test_adj_632_23(self):
        results = self.derivation.derive(word_b='уравниловка', pos_b='noun', pos_a='adj')
        self.assertIn('уравниловский', results)
        results = self.derivation.derive(word_b='мальчишка', pos_b='noun', pos_a='adj')
        self.assertIn('мальчишеский', results)
        results = self.derivation.derive(word_b='Новогрудок', pos_b='noun', pos_a='adj')
        self.assertIn('новогрудский', results)

    def test_adj_632_24(self):
        results = self.derivation.derive(word_b='переводчик', pos_b='noun', pos_a='adj')
        self.assertIn('переводческий', results)

    def test_adj_632_25(self):
        results = self.derivation.derive(word_b='анахронизм', pos_b='noun', pos_a='adj')
        self.assertIn('анахронический', results)

    def test_adj_632_26(self):
        results = self.derivation.derive(word_b='космос', pos_b='noun', pos_a='adj')
        self.assertIn('космический', results)
        results = self.derivation.derive(word_b='синтаксис', pos_b='noun', pos_a='adj')
        self.assertIn('синтаксический', results)
        results = self.derivation.derive(word_b='апокалипсис', pos_b='noun', pos_a='adj')
        self.assertIn('апокалиптический', results)

    def test_adj_632_27(self):
        results = self.derivation.derive(word_b='женщина', pos_b='noun', pos_a='adj')
        self.assertIn('женский', results)
        results = self.derivation.derive(word_b='мужчина', pos_b='noun', pos_a='adj')
        self.assertIn('мужской', results)

    def test_adj_632_28(self):
        results = self.derivation.derive(word_b='свинья', pos_b='noun', pos_a='adj')
        self.assertIn('свинский', results)
        results = self.derivation.derive(word_b='каналья', pos_b='noun', pos_a='adj')
        self.assertIn('канальский', results)

    def test_adj_632_29(self):
        results = self.derivation.derive(word_b='Терек', pos_b='noun', pos_a='adj')
        self.assertIn('терский', results)
        results = self.derivation.derive(word_b='Польша', pos_b='noun', pos_a='adj')
        self.assertIn('польский', results)

    def test_adj_632_30(self):
        results = self.derivation.derive(word_b='язычник', pos_b='noun', pos_a='adj')
        self.assertIn('языческий', results)

    def test_adj_632_31(self):
        results = self.derivation.derive(word_b='господин', pos_b='noun', pos_a='adj')
        self.assertIn('господский', results)
        results = self.derivation.derive(word_b='татарин', pos_b='noun', pos_a='adj')
        self.assertIn('татарский', results)
        results = self.derivation.derive(word_b='крестьянин', pos_b='noun', pos_a='adj')
        self.assertIn('крестьянский', results)
        results = self.derivation.derive(word_b='хозяин', pos_b='noun', pos_a='adj')
        self.assertIn('хозяйский', results)

    def test_adj_632_32(self):
        results = self.derivation.derive(word_b='матерь', pos_b='noun', pos_a='adj')
        self.assertIn('материнский', results)
        results = self.derivation.derive(word_b='ребята', pos_b='noun', pos_a='adj')
        self.assertIn('ребяческий', results)

    def test_adj_632_33(self):
        results = self.derivation.derive(word_b='драма', pos_b='noun', pos_a='adj')
        self.assertIn('драматический', results)
        results = self.derivation.derive(word_b='симптом', pos_b='noun', pos_a='adj')
        self.assertIn('симптоматический', results)

    def test_adj_632_34(self):
        results = self.derivation.derive(word_b='арго', pos_b='noun', pos_a='adj')
        self.assertIn('арготический', results)

    def test_adj_632_35(self):
        results = self.derivation.derive(word_b='Неаполь', pos_b='noun', pos_a='adj')
        self.assertIn('неаполитанский', results)
        results = self.derivation.derive(word_b='негр', pos_b='noun', pos_a='adj')
        self.assertIn('негритянский', results)

    def test_adj_632_36(self):
        results = self.derivation.derive(word_b='персы', pos_b='noun', pos_a='adj')
        self.assertIn('персидский', results)

    def test_adj_632_37(self):
        results = self.derivation.derive(word_b='алгебра', pos_b='noun', pos_a='adj')
        self.assertIn('алгебраический', results)
        results = self.derivation.derive(word_b='проза', pos_b='noun', pos_a='adj')
        self.assertIn('прозаический', results)

    def test_adj_632_38(self):
        results = self.derivation.derive(word_b='захватчик', pos_b='noun', pos_a='adj')
        self.assertIn('захватнический', results)

    def test_adj_632_39(self):
        results = self.derivation.derive(word_b='турок', pos_b='noun', pos_a='adj')
        self.assertIn('турецкий', results)

    def test_adj_632_40(self):
        results = self.derivation.derive(word_b='депо', pos_b='noun', pos_a='adj')
        self.assertIn('деповский', results)
        results = self.derivation.derive(word_b='Пикассо', pos_b='noun', pos_a='adj')
        self.assertIn('пикассовский', results)
        results = self.derivation.derive(word_b='Гёте', pos_b='noun', pos_a='adj')
        self.assertIn('гётевский', results)
        results = self.derivation.derive(word_b='Лахти', pos_b='noun', pos_a='adj')
        self.assertIn('лахтинский', results)
        results = self.derivation.derive(word_b='Тольятти', pos_b='noun', pos_a='adj')
        self.assertIn('тольяттинский', results)
        results = self.derivation.derive(word_b='Гоа', pos_b='noun', pos_a='adj')
        self.assertIn('гоанский', results)
        results = self.derivation.derive(word_b='Никарагуа', pos_b='noun', pos_a='adj')
        self.assertIn('никарагуанский', results)
        results = self.derivation.derive(word_b='Чили', pos_b='noun', pos_a='adj')
        self.assertIn('чилийский', results)
        results = self.derivation.derive(word_b='Токио', pos_b='noun', pos_a='adj')
        self.assertIn('токийский', results)

    def test_adj_632_41(self):
        results = self.derivation.derive(word_b='Свердловск', pos_b='noun', pos_a='adj')
        self.assertIn('свердловский', results)
        results = self.derivation.derive(word_b='Донецк', pos_b='noun', pos_a='adj')
        self.assertIn('донецкий', results)
        results = self.derivation.derive(word_b='Белинский', pos_b='noun', pos_a='adj')
        self.assertIn('белинский', results)
        results = self.derivation.derive(word_b='Вешенская', pos_b='noun', pos_a='adj')
        self.assertIn('вешенский', results)

    def test_adj_632_42(self):
        results = self.derivation.derive(word_b='саксы', pos_b='noun', pos_a='adj')
        self.assertIn('сакский', results)
        results = self.derivation.derive(word_b='Прованс', pos_b='noun', pos_a='adj')
        self.assertIn('прованский', results)
        results = self.derivation.derive(word_b='Уэльс', pos_b='noun', pos_a='adj')
        self.assertIn('уэльский', results)
        results = self.derivation.derive(word_b='Пруссия', pos_b='noun', pos_a='adj')
        self.assertIn('прусский', results)
        results = self.derivation.derive(word_b='пруссы', pos_b='noun', pos_a='adj')
        self.assertIn('прусский', results)

    def test_adj_632_43(self):
        results = self.derivation.derive(word_b='ткач', pos_b='noun', pos_a='adj')
        self.assertIn('ткацкий', results)

    def test_adj_632_44(self):
        results = self.derivation.derive(word_b='чукчи', pos_b='noun', pos_a='adj')
        self.assertIn('чукотский', results)

    def test_adj_632_45(self):
        results = self.derivation.derive(word_b='ребята', pos_b='noun', pos_a='adj')
        self.assertIn('ребяческий', results)
        results = self.derivation.derive(word_b='студент', pos_b='noun', pos_a='adj')
        self.assertIn('студенческий', results)
        results = self.derivation.derive(word_b='метеорит', pos_b='noun', pos_a='adj')
        self.assertIn('метеорический', results)
        results = self.derivation.derive(word_b='князь', pos_b='noun', pos_a='adj')
        self.assertIn('княжеский', results)

    def test_adj_632_46(self):
        results = self.derivation.derive(word_b='Орда', pos_b='noun', pos_a='adj')
        self.assertIn('ордынский', results)

    def test_adj_632_47(self):
        results = self.derivation.derive(word_b='хаос', pos_b='noun', pos_a='adj')
        self.assertIn('хаотический', results)
        results = self.derivation.derive(word_b='анализ', pos_b='noun', pos_a='adj')
        self.assertIn('аналитический', results)
        results = self.derivation.derive(word_b='сарказм', pos_b='noun', pos_a='adj')
        self.assertIn('саркастический', results)
        results = self.derivation.derive(word_b='большевизм', pos_b='noun', pos_a='adj')
        self.assertIn('большевистский', results)

    def test_adj_632_48(self):
        results = self.derivation.derive(word_b='Флоренция', pos_b='noun', pos_a='adj')
        self.assertIn('флорентийский', results)
        results = self.derivation.derive(word_b='Далмация', pos_b='noun', pos_a='adj')
        self.assertIn('далматинский', results)

    def test_adj_632_49(self):
        results = self.derivation.derive(word_b='диагноз', pos_b='noun', pos_a='adj')
        self.assertIn('диагностический', results)
        results = self.derivation.derive(word_b='парафраз', pos_b='noun', pos_a='adj')
        self.assertIn('парафрастический', results)

    def test_adj_632_50(self):
        results = self.derivation.derive(word_b='юрист', pos_b='noun', pos_a='adj')
        self.assertIn('юридический', results)

    def test_adj_632_50(self):
        results = self.derivation.derive(word_b='деляга', pos_b='noun', pos_a='adj')
        self.assertIn('деляческий', results)

    def test_adj_632_51(self):
        results = self.derivation.derive(word_b='Дания', pos_b='noun', pos_a='adj')
        self.assertIn('датский', results)

    def test_adj_632_52(self):
        results = self.derivation.derive(word_b='деревня', pos_b='noun', pos_a='adj')
        self.assertIn('деревенский', results)
        results = self.derivation.derive(word_b='страдалец', pos_b='noun', pos_a='adj')
        self.assertIn('страдальческий', results)

    def test_adj_632_53(self):
        results = self.derivation.derive(word_b='отец', pos_b='noun', pos_a='adj')
        self.assertIn('отеческий', results)

    def test_adj_632_54(self):
        results = self.derivation.derive(word_b='министр', pos_b='noun', pos_a='adj')
        self.assertIn('министерский', results)
        results = self.derivation.derive(word_b='житьё', pos_b='noun', pos_a='adj')
        self.assertIn('житейский', results)
        results = self.derivation.derive(word_b='шляхта', pos_b='noun', pos_a='adj')
        self.assertIn('шляхетский', results)
        results = self.derivation.derive(word_b='Соловки', pos_b='noun', pos_a='adj')
        self.assertIn('соловецкий', results)
        results = self.derivation.derive(word_b='Венгрия', pos_b='noun', pos_a='adj')
        self.assertIn('венгерский', results)
        results = self.derivation.derive(word_b='чечня', pos_b='noun', pos_a='adj')
        self.assertIn('чеченский', results)

    def test_adj_632_55(self):
        results = self.derivation.derive(word_b='бургомистр', pos_b='noun', pos_a='adj')
        self.assertIn('бургомистерский', results)
        results = self.derivation.derive(word_b='магистр', pos_b='noun', pos_a='adj')
        self.assertIn('магистерский', results)
        results = self.derivation.derive(word_b='Коломна', pos_b='noun', pos_a='adj')
        self.assertIn('коломенский', results)
        results = self.derivation.derive(word_b='Вязьма', pos_b='noun', pos_a='adj')
        self.assertIn('вяземский', results)
        results = self.derivation.derive(word_b='Опочка', pos_b='noun', pos_a='adj')
        self.assertIn('опочецкий', results)
        results = self.derivation.derive(word_b='Песочня', pos_b='noun', pos_a='adj')
        self.assertIn('песоченский', results)

    def test_adj_632_56(self):
        results = self.derivation.derive(word_b='Москва', pos_b='noun', pos_a='adj')
        self.assertIn('московский', results)
        results = self.derivation.derive(word_b='Вологда', pos_b='noun', pos_a='adj')
        self.assertIn('вологодский', results)
        results = self.derivation.derive(word_b='Вытегра', pos_b='noun', pos_a='adj')
        self.assertIn('вытегорский', results)
        results = self.derivation.derive(word_b='Вычегда', pos_b='noun', pos_a='adj')
        self.assertIn('вычегодский', results)
        results = self.derivation.derive(word_b='Литва', pos_b='noun', pos_a='adj')
        self.assertIn('литовский', results)
        results = self.derivation.derive(word_b='мордва', pos_b='noun', pos_a='adj')
        self.assertIn('мордовский', results)
        results = self.derivation.derive(word_b='чухна', pos_b='noun', pos_a='adj')
        self.assertIn('чухонский', results)
        results = self.derivation.derive(word_b='угры', pos_b='noun', pos_a='adj')
        self.assertIn('угорский', results)
        results = self.derivation.derive(word_b='чукчи', pos_b='noun', pos_a='adj')
        self.assertIn('чукотский', results)

    def test_adj_632_57(self):
        results = self.derivation.derive(word_b='армия', pos_b='noun', pos_a='adj')
        self.assertIn('армейский', results)
        results = self.derivation.derive(word_b='библия', pos_b='noun', pos_a='adj')
        self.assertIn('библейский', results)
        results = self.derivation.derive(word_b='артиллерия', pos_b='noun', pos_a='adj')
        self.assertIn('артиллерийский', results)

    def test_adj_632_58(self):
        results = self.derivation.derive(word_b='Италия', pos_b='noun', pos_a='adj')
        self.assertIn('итальянский', results)

    def test_adj_636(self):
        results = self.derivation.derive(word_b='Кант', pos_b='noun', pos_a='adj')
        self.assertIn('кантианский', results)
        results = self.derivation.derive(word_b='Фейербах', pos_b='noun', pos_a='adj')
        self.assertIn('фейербахианский', results)
        results = self.derivation.derive(word_b='Ломброзо', pos_b='noun', pos_a='adj')
        self.assertIn('ломброзианский', results)

    def test_adj_636_2(self):
        results = self.derivation.derive(word_b='Мальтус', pos_b='noun', pos_a='adj')
        self.assertIn('мальтузианский', results)

    def test_adj_636_3(self):
        results = self.derivation.derive(word_b='Вольтер', pos_b='noun', pos_a='adj')
        self.assertIn('вольтерьянский', results)
        results = self.derivation.derive(word_b='Гегель', pos_b='noun', pos_a='adj')
        self.assertIn('гегельянский', results)
        results = self.derivation.derive(word_b='Фихте', pos_b='noun', pos_a='adj')
        self.assertIn('фихтеанский', results)
        results = self.derivation.derive(word_b='Ницше', pos_b='noun', pos_a='adj')
        self.assertIn('ницшеанский', results)
        results = self.derivation.derive(word_b='Конфуций', pos_b='noun', pos_a='adj')
        self.assertIn('конфуцианский', results)

    def test_adj_636_4(self):
        results = self.derivation.derive(word_b='Вакх', pos_b='noun', pos_a='adj')
        self.assertIn('вакхический', results)
        results = self.derivation.derive(word_b='Байрон', pos_b='noun', pos_a='adj')
        self.assertIn('байронический', results)

    def test_adj_636_5(self):
        results = self.derivation.derive(word_b='Будда', pos_b='noun', pos_a='adj')
        self.assertIn('буддийский', results)

    def test_adj_636_6(self):
        results = self.derivation.derive(word_b='Пифагор', pos_b='noun', pos_a='adj')
        self.assertIn('пифагорейский', results)

    def test_adj_637(self):
        results = self.derivation.derive(word_b='голова', pos_b='noun', pos_a='adj')
        self.assertIn('головастый', results)
        results = self.derivation.derive(word_b='лоб', pos_b='noun', pos_a='adj')
        self.assertIn('лобастый', results)
        results = self.derivation.derive(word_b='горло', pos_b='noun', pos_a='adj')
        self.assertIn('горластый', results)
        results = self.derivation.derive(word_b='ноздря', pos_b='noun', pos_a='adj')
        self.assertIn('ноздрястый', results)
        results = self.derivation.derive(word_b='щека', pos_b='noun', pos_a='adj')
        self.assertIn('щекастый', results)
        results = self.derivation.derive(word_b='язык', pos_b='noun', pos_a='adj')
        self.assertIn('языкастый', results)
        results = self.derivation.derive(word_b='ухо', pos_b='noun', pos_a='adj')
        self.assertIn('ушастый', results)
        results = self.derivation.derive(word_b='щель', pos_b='noun', pos_a='adj')
        self.assertIn('щелястый', results)
        results = self.derivation.derive(word_b='мышь', pos_b='noun', pos_a='adj')
        self.assertIn('мышастый', results)
        results = self.derivation.derive(word_b='очки', pos_b='noun', pos_a='adj')
        self.assertIn('очкастый', results)
        results = self.derivation.derive(word_b='грудь', pos_b='noun', pos_a='adj')
        self.assertIn('грудастый', results)

    def test_adj_637_2(self):
        results = self.derivation.derive(word_b='вихор', pos_b='noun', pos_a='adj')
        self.assertIn('вихрастый', results)
        results = self.derivation.derive(word_b='пенсне', pos_b='noun', pos_a='adj')
        self.assertIn('пенснястый', results)

    def test_adj_638(self):
        results = self.derivation.derive(word_b='зуб', pos_b='noun', pos_a='adj')
        self.assertIn('зубатый', results)
        results = self.derivation.derive(word_b='борода', pos_b='noun', pos_a='adj')
        self.assertIn('бородатый', results)
        results = self.derivation.derive(word_b='гор', pos_b='noun', pos_a='adj')
        self.assertIn('рогатый', results)
        results = self.derivation.derive(word_b='хохол', pos_b='noun', pos_a='adj')
        self.assertIn('хохлатый', results)
        results = self.derivation.derive(word_b='язык', pos_b='noun', pos_a='adj')
        self.assertIn('языкатый', results)
        results = self.derivation.derive(word_b='пузо', pos_b='noun', pos_a='adj')
        self.assertIn('пузатый', results)
        results = self.derivation.derive(word_b='брюхо', pos_b='noun', pos_a='adj')
        self.assertIn('брюхатый', results)

    def test_adj_638_2(self):
        results = self.derivation.derive(word_b='внук', pos_b='noun', pos_a='adj')
        self.assertIn('внучатый', results)

    def test_adj_638_3(self):
        results = self.derivation.derive(word_b='щербина', pos_b='noun', pos_a='adj')
        self.assertIn('щербатый', results)
        results = self.derivation.derive(word_b='желвак', pos_b='noun', pos_a='adj')
        self.assertIn('желватый', results)

    def test_adj_638_4(self):
        results = self.derivation.derive(word_b='перо', pos_b='noun', pos_a='adj')
        self.assertIn('пернатый', results)

    def test_adj_639(self):
        results = self.derivation.derive(word_b='свод', pos_b='noun', pos_a='adj')
        self.assertIn('сводчатый', results)
        results = self.derivation.derive(word_b='бахрома', pos_b='noun', pos_a='adj')
        self.assertIn('бахромчатый', results)
        results = self.derivation.derive(word_b='колено', pos_b='noun', pos_a='adj')
        self.assertIn('коленчатый', results)
        results = self.derivation.derive(word_b='материя', pos_b='noun', pos_a='adj')
        self.assertIn('матерчатый', results)
        results = self.derivation.derive(word_b='нить', pos_b='noun', pos_a='adj')
        self.assertIn('нитчатый', results)
        results = self.derivation.derive(word_b='бревно', pos_b='noun', pos_a='adj')
        self.assertIn('бревенчатый', results)
        results = self.derivation.derive(word_b='доска', pos_b='noun', pos_a='adj')
        self.assertIn('дощатый', results)
        results = self.derivation.derive(word_b='зубец', pos_b='noun', pos_a='adj')
        self.assertIn('зубчатый', results)
        results = self.derivation.derive(word_b='крупица', pos_b='noun', pos_a='adj')
        self.assertIn('крупчатый', results)
        results = self.derivation.derive(word_b='бугорок', pos_b='noun', pos_a='adj')
        self.assertIn('бугорчатый', results)
        results = self.derivation.derive(word_b='желёзка', pos_b='noun', pos_a='adj')
        self.assertIn('желёзчатый', results)
        results = self.derivation.derive(word_b='веснушки', pos_b='noun', pos_a='adj')
        self.assertIn('веснушчатый', results)
        results = self.derivation.derive(word_b='кубышка', pos_b='noun', pos_a='adj')
        self.assertIn('кубышчатый', results)

    def test_adj_639_2(self):
        results = self.derivation.derive(word_b='губка', pos_b='noun', pos_a='adj')
        self.assertIn('губчатый', results)
        results = self.derivation.derive(word_b='ресница', pos_b='noun', pos_a='adj')
        self.assertIn('реснитчатый', results)
        results = self.derivation.derive(word_b='вилы', pos_b='noun', pos_a='adj')
        self.assertIn('вильчатый', results)
        results = self.derivation.derive(word_b='стрелка', pos_b='noun', pos_a='adj')
        self.assertIn('стрельчатый', results)
        results = self.derivation.derive(word_b='угол', pos_b='noun', pos_a='adj')
        self.assertIn('угольчатый', results)
        results = self.derivation.derive(word_b='глазок', pos_b='noun', pos_a='adj')
        self.assertIn('глазчатый', results)
        results = self.derivation.derive(word_b='хлопья', pos_b='noun', pos_a='adj')
        self.assertIn('хлопчатый', results)

    def test_adj_639_3(self):
        results = self.derivation.derive(word_b='крапина', pos_b='noun', pos_a='adj')
        self.assertIn('крапчатый', results)

    def test_adj_640(self):
        results = self.derivation.derive(word_b='игла', pos_b='noun', pos_a='adj')
        self.assertIn('игловатый', results)
        results = self.derivation.derive(word_b='плут', pos_b='noun', pos_a='adj')
        self.assertIn('плутоватый', results)
        results = self.derivation.derive(word_b='стекло', pos_b='noun', pos_a='adj')
        self.assertIn('стекловатый', results)
        results = self.derivation.derive(word_b='щеголь', pos_b='noun', pos_a='adj')
        self.assertIn('щеголеватый', results)
        results = self.derivation.derive(word_b='кочка', pos_b='noun', pos_a='adj')
        self.assertIn('кочковатый', results)
        results = self.derivation.derive(word_b='мужик', pos_b='noun', pos_a='adj')
        self.assertIn('мужиковатый', results)
        results = self.derivation.derive(word_b='крючок', pos_b='noun', pos_a='adj')
        self.assertIn('крючковатый', results)
        results = self.derivation.derive(word_b='прыщ', pos_b='noun', pos_a='adj')
        self.assertIn('прыщеватый', results)
        results = self.derivation.derive(word_b='солнце', pos_b='noun', pos_a='adj')
        self.assertIn('солнцеватый', results)
        results = self.derivation.derive(word_b='молодец', pos_b='noun', pos_a='adj')
        self.assertIn('молодцеватый', results)
        results = self.derivation.derive(word_b='пыль', pos_b='noun', pos_a='adj')
        self.assertIn('пылеватый', results)
        results = self.derivation.derive(word_b='кудри', pos_b='noun', pos_a='adj')
        self.assertIn('кудреватый', results)

    def test_adj_640_2(self):
        results = self.derivation.derive(word_b='смола', pos_b='noun', pos_a='adj')
        self.assertIn('смолеватый', results)
        results = self.derivation.derive(word_b='зверь', pos_b='noun', pos_a='adj')
        self.assertIn('звероватый', results)

    def test_adj_640_3(self):
        results = self.derivation.derive(word_b='веснушки', pos_b='noun', pos_a='adj')
        self.assertIn('весноватый', results)

    def test_adj_640_4(self):
        results = self.derivation.derive(word_b='бес', pos_b='noun', pos_a='adj')
        self.assertIn('бесноватый', results)

    def test_adj_641(self):
        results = self.derivation.derive(word_b='дар', pos_b='noun', pos_a='adj')
        self.assertIn('даровитый', results)
        results = self.derivation.derive(word_b='башка', pos_b='noun', pos_a='adj')
        self.assertIn('башковитый', results)
        results = self.derivation.derive(word_b='пух', pos_b='noun', pos_a='adj')
        self.assertIn('пуховитый', results)
        results = self.derivation.derive(word_b='бочок', pos_b='noun', pos_a='adj')
        self.assertIn('бочковитый', results)
        results = self.derivation.derive(word_b='дкло', pos_b='noun', pos_a='adj')
        self.assertIn('деловитый', results)
        results = self.derivation.derive(word_b='глянец', pos_b='noun', pos_a='adj')
        self.assertIn('глянцевитый', results)

    def test_adj_642(self):
        results = self.derivation.derive(word_b='морщина', pos_b='noun', pos_a='adj')
        self.assertIn('морщинистый', results)
        results = self.derivation.derive(word_b='лёд', pos_b='noun', pos_a='adj')
        self.assertIn('льдистый', results)
        results = self.derivation.derive(word_b='дупло', pos_b='noun', pos_a='adj')
        self.assertIn('дуплистый', results)
        results = self.derivation.derive(word_b='коготь', pos_b='noun', pos_a='adj')
        self.assertIn('когтистый', results)
        results = self.derivation.derive(word_b='творог', pos_b='noun', pos_a='adj')
        self.assertIn('творожистый', results)
        results = self.derivation.derive(word_b='ёрш', pos_b='noun', pos_a='adj')
        self.assertIn('ершистый', results)
        results = self.derivation.derive(word_b='плечо', pos_b='noun', pos_a='adj')
        self.assertIn('плечистый', results)
        results = self.derivation.derive(word_b='змея', pos_b='noun', pos_a='adj')
        self.assertIn('змеистый', results)
        results = self.derivation.derive(word_b='слой', pos_b='noun', pos_a='adj')
        self.assertIn('слоистый', results)
        results = self.derivation.derive(word_b='тень', pos_b='noun', pos_a='adj')
        self.assertIn('тенистый', results)
        results = self.derivation.derive(word_b='мускулы', pos_b='noun', pos_a='adj')
        self.assertIn('мускулистый', results)
        results = self.derivation.derive(word_b='чутьё', pos_b='noun', pos_a='adj')
        self.assertIn('чутьистый', results)
        results = self.derivation.derive(word_b='суглинок', pos_b='noun', pos_a='adj')
        self.assertIn('суглинистый', results)
        results = self.derivation.derive(word_b='сноровка', pos_b='noun', pos_a='adj')
        self.assertIn('сноровистый', results)
        results = self.derivation.derive(word_b='терние', pos_b='noun', pos_a='adj')
        self.assertIn('тернистый', results)
        results = self.derivation.derive(word_b='кремний', pos_b='noun', pos_a='adj')
        self.assertIn('кремнистый', results)

    def test_adj_642_2(self):
        results = self.derivation.derive(word_b='седловина', pos_b='noun', pos_a='adj')
        self.assertIn('седлистый', results)
        results = self.derivation.derive(word_b='скважина', pos_b='noun', pos_a='adj')
        self.assertIn('скважистый', results)
        results = self.derivation.derive(word_b='щетина', pos_b='noun', pos_a='adj')
        self.assertIn('щетинистый', results)

    def test_adj_642_3(self):
        results = self.derivation.derive(word_b='ущелье', pos_b='noun', pos_a='adj')
        self.assertIn('ущелистый', results)
        results = self.derivation.derive(word_b='иней', pos_b='noun', pos_a='adj')
        self.assertIn('инистый', results)

    def test_adj_642_4(self):
        results = self.derivation.derive(word_b='шаг', pos_b='noun', pos_a='adj')
        self.assertIn('шагистый', results)

    def test_adj_642_5(self):
        results = self.derivation.derive(word_b='камень', pos_b='noun', pos_a='adj')
        self.assertIn('каменистый', results)

    def test_adj_643(self):
        results = self.derivation.derive(word_b='слеза', pos_b='noun', pos_a='adj')
        self.assertIn('слезливый', results)
        results = self.derivation.derive(word_b='плакса', pos_b='noun', pos_a='adj')
        self.assertIn('плаксивый', results)
        results = self.derivation.derive(word_b='талант', pos_b='noun', pos_a='adj')
        self.assertIn('талантливый', results)
        results = self.derivation.derive(word_b='сопля', pos_b='noun', pos_a='adj')
        self.assertIn('сопливый', results)
        results = self.derivation.derive(word_b='дождь', pos_b='noun', pos_a='adj')
        self.assertIn('дождливый', results)
        results = self.derivation.derive(word_b='засуха', pos_b='noun', pos_a='adj')
        self.assertIn('засушливый', results)
        results = self.derivation.derive(word_b='зяблик', pos_b='noun', pos_a='adj')
        self.assertIn('зябличивый', results)
        results = self.derivation.derive(word_b='добыча', pos_b='noun', pos_a='adj')
        self.assertIn('добычливый', results)
        results = self.derivation.derive(word_b='затея', pos_b='noun', pos_a='adj')
        self.assertIn('затейливый', results)
        results = self.derivation.derive(word_b='совесть', pos_b='noun', pos_a='adj')
        self.assertIn('совестливый', results)
        results = self.derivation.derive(word_b='фальшь', pos_b='noun', pos_a='adj')
        self.assertIn('фальшивый', results)
        results = self.derivation.derive(word_b='удой', pos_b='noun', pos_a='adj')
        self.assertIn('удойливый', results)
        results = self.derivation.derive(word_b='ложь', pos_b='noun', pos_a='adj')
        self.assertIn('лживый', results)
        results = self.derivation.derive(word_b='червь', pos_b='noun', pos_a='adj')
        self.assertIn('червивый', results)
        results = self.derivation.derive(word_b='противоречие', pos_b='noun', pos_a='adj')
        self.assertIn('противоречивый', results)
        results = self.derivation.derive(word_b='вша', pos_b='noun', pos_a='adj')
        self.assertIn('вшивый', results)

    def test_adj_643_2(self):
        results = self.derivation.derive(word_b='боязнь', pos_b='noun', pos_a='adj')
        self.assertIn('боязливый', results)

    def test_adj_643_3(self):
        results = self.derivation.derive(word_b='тоска', pos_b='noun', pos_a='adj')
        self.assertIn('тоскливый', results)
        results = self.derivation.derive(word_b='визг', pos_b='noun', pos_a='adj')
        self.assertIn('визгливый', results)
        results = self.derivation.derive(word_b='крик', pos_b='noun', pos_a='adj')
        self.assertIn('крикливый', results)

    def test_adj_643_4(self):
        results = self.derivation.derive(word_b='ребята', pos_b='noun', pos_a='adj')
        self.assertIn('ребячливый', results)

    def test_adj_643_5(self):
        results = self.derivation.derive(word_b='участие', pos_b='noun', pos_a='adj')
        self.assertIn('участливый', results)
        results = self.derivation.derive(word_b='счастье', pos_b='noun', pos_a='adj')
        self.assertIn('счастливый', results)
        results = self.derivation.derive(word_b='смётка', pos_b='noun', pos_a='adj')
        self.assertIn('сметливый', results)

    def test_adj_644(self):
        results = self.derivation.derive(word_b='ржа', pos_b='noun', pos_a='adj')
        self.assertIn('ржавый', results)
        results = self.derivation.derive(word_b='прыщ', pos_b='noun', pos_a='adj')
        self.assertIn('прыщавый', results)
        results = self.derivation.derive(word_b='слюна', pos_b='noun', pos_a='adj')
        self.assertIn('слюнявый', results)
        results = self.derivation.derive(word_b='кудри', pos_b='noun', pos_a='adj')
        self.assertIn('кудрявый', results)
        results = self.derivation.derive(word_b='писк', pos_b='noun', pos_a='adj')
        self.assertIn('писклявый', results)
        results = self.derivation.derive(word_b='труха', pos_b='noun', pos_a='adj')
        self.assertIn('трухлявый', results)
        results = self.derivation.derive(word_b='кости', pos_b='noun', pos_a='adj')
        self.assertIn('костлявый', results)
        results = self.derivation.derive(word_b='сучья', pos_b='noun', pos_a='adj')
        self.assertIn('сучлявый', results)

    def test_adj_644_2(self):
        results = self.derivation.derive(word_b='кровь', pos_b='noun', pos_a='adj')
        self.assertIn('кровавый', results)
        results = self.derivation.derive(word_b='дыра', pos_b='noun', pos_a='adj')
        self.assertIn('дырявый', results)

    def test_adj_644_3(self):
        results = self.derivation.derive(word_b='величие', pos_b='noun', pos_a='adj')
        self.assertIn('величавый', results)

    def test_adj_645_1(self):
        results = self.derivation.derive(word_b='жар', pos_b='noun', pos_a='adj')
        self.assertIn('жаркий', results)
        results = self.derivation.derive(word_b='жара', pos_b='noun', pos_a='adj')
        self.assertIn('жаркий', results)
        results = self.derivation.derive(word_b='зной', pos_b='noun', pos_a='adj')
        self.assertIn('знойкий', results)

    def test_adj_645_2(self):
        results = self.derivation.derive(word_b='зрение', pos_b='noun', pos_a='adj')
        self.assertIn('зоркий', results)

    def test_adj_645_3(self):
        results = self.derivation.derive(word_b='зрение', pos_b='noun', pos_a='adj')
        self.assertIn('зрячий', results)

    def test_adj_645_4(self):
        results = self.derivation.derive(word_b='зрение', pos_b='noun', pos_a='adj')
        self.assertIn('зримый', results)

    def test_adj_645_5(self):
        results = self.derivation.derive(word_b='круг', pos_b='noun', pos_a='adj')
        self.assertIn('круглый', results)
        results = self.derivation.derive(word_b='свет', pos_b='noun', pos_a='adj')
        self.assertIn('светлый', results)

    def test_adj_645_6(self):
        results = self.derivation.derive(word_b='год', pos_b='noun', pos_a='adj')
        self.assertIn('годовалый', results)

    def test_adj_645_7(self):
        results = self.derivation.derive(word_b='имя', pos_b='noun', pos_a='adj')
        self.assertIn('именитый', results)


if __name__ == '__main__':
    unittest.main(verbosity=2)
