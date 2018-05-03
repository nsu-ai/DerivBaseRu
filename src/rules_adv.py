from functions import *

rules_all = {
    'adv': [

    # СУФФИКСАЛЬНЫЕ НАРЕЧИЯ
    # НАРЕЧИЯ, МОТИВИРОВАННЫЕ ПРИЛАГАТЕЛЬНЫМИ

    # 977
    Rule(
        pos_b='adj', pos_a='adv',
        rules=[
            (excsfx, {'ский', 'ской', 'цкий', 'цкой'}),
            (
                [
                    (delsfx, {'ый', 'ой'}),
                    (addsfx, {'о'})
                ],
                [
                    (delsfx, {'ий'}),
                    (addsfx, {'о', 'е'})
                ],
            )
        ]
    ),

    # 979
    Rule(
        pos_b='adj', pos_a='adv',
        rules=[
            (onlysfx, {'ский', 'ской', 'цкий', 'цкой', 'ий'}),
            (
                [
                    (onlysfx, {'ский', 'ской', 'цкий', 'цкой'}),
                    (delsfx, {'ий', 'ой'}),
                ],
                [
                    (excsfx, {'ский', 'ской', 'цкий', 'цкой'}),
                    (delsfx, {'ий'}),
                    (soft, 'opt'),
                ]
            ),
            (addsfx, {'и'})
        ]
    ),


    # НАРЕЧИЯ, МОТИВИРОВАННЫЕ СУЩЕСТВИТЕЛЬНЫМИ

    # 982

    Rule(
        pos_b='noun', pos_a='adv',
        rules=[
            (
                [
                    (delsfx, {'ь'}),
                    (delvowel, 'opt'),  # день - днём, пень - пнём
                    (addsfx, {'ём', 'ем'})
                ],
		[
                    (onlysfx, {'ь'}),
                    (addsfx, {'ю'})
                ],
                [
                    (onlysfx, consonants | {'о'}),
                    (delsfx, 'try', {'о'}),
                    (delvowel, 'opt'),
                    (addsfx, {'ом', 'ем', 'ём'})
                ],
                [
                    (onlysfx, {'а'}),
		    (delsfx, {'а'}),
		    (
		        [
			    (onlysfx, sh | {'ц'}),
			    (addsfx, {'ей'})
		        ],
		        [
			    (excsfx, sh),
			    (addsfx, {'ой', 'ою'})
		        ],
		    ),
                ],
            )
        ]
    ),

    # НАРЕЧИЯ, МОТИВИРОВАННЫЕ ЧИСЛИТЕЛЬНЫМИ



    # НАРЕЧИЯ, МОТИВИРОВАННЫЕ ГЛАГОЛАМИ

    # 985

    Rule(
        pos_b='verb', pos_a='adv',
        rules=[
            (delsfx, {'ть'}),
            (
                (delsfx, {'а', 'е'}),
                (replsfx, 'try', {('я', 'й'), ('и', 'ь')}),
            ),
            (addsfx, {'мя'})
        ]
    ),

    # НАРЕЧИЯ, МОТИВИРОВАННЫЕ НАРЕЧИЯМИ

    # 988

    Rule(
        pos_b='adv', pos_a='adv',
        rules=[
            (delsfx, {'о'}),
            (addsfx, {'овато'})
        ]
    ),

    # 989

    Rule(
        pos_b='adv', pos_a='adv',
        rules=[
            (delsfx, {'о'}),
            (delsfx, 'opt', {'к'}),
            (
                [
                    (onlysfx, velar),
                    (addsfx, {'онько', 'енько'})
                ],
                [
                    (onlysfx, consonants - velar),
                    (addsfx, {'енько'})
                ],
            )
        ]
    ),

    # 990
    Rule(
        pos_b='adv', pos_a='adv',
        rules=[
            (delsfx, {'о'}),
            (delsfx, 'opt', {'к'}),
            (addsfx, {'ёхонько', 'ёшенько'})

        ]
    ),

    # 991
    Rule(
        pos_b='adv', pos_a='adv',
        rules=[
            (
                [
                    (onlysfx, {'ом'}),
                    (delsfx, {'ом'}),
                    (addvowel, 'try'),
                    (plt, 'try'),
                    (addsfx, {'ком'}),
                ],
                [
                    (onlysfx, {'ой'}),
                    (delsfx, {'ой'}),
                    (addvowel, 'try'),
                    (plt, 'try'),
                    (addsfx, {'кой'}),
                ],
                [
                    (onlysfx, {'у'}),
                    (delsfx, {'у'}),
                    (addvowel, 'try'),
                    (plt, 'try'),
                    (addsfx, {'ку'}),
                ],
                [
                    (onlysfx, {'енько', 'онько'}),
                    (delsfx, {'о'}),
                    (addvowel, 'try'),
                    (plt, 'try'),
                    (addsfx, {'ко'}),
                ],
            )
        ]
    ),

    # ПРЕФИКСАЛЬНЫЕ НАРЕЧИЯ

    # 992
    Rule(
        pos_b='adv', pos_a='adv',
        rules=[
            (addpfx, {'не'})
        ]
    ),


    # ПРЕФИКСАЛЬНО-СУФФИКСАЛЬНЫЕ НАРЕЧИЯ

    # НАРЕЧИЯ, МОТИВИРОВАННЫЕ ПРИЛАГАТЕЛЬНЫМИ

    # 994
    Rule(
        pos_b='adj', pos_a='adv',
        rules=[
            (addpfx, {'по-'}),
            (
                [
                    (delsfx, {'ый', 'ой', 'ий'}),
                    (addsfx, {'ому'})
                ],
                [
                    (delsfx, {'ий'}),
                    (soft, 'opt'),
                    (addsfx, {'ему'})
                ]
            )
        ]
    ),

    # 995
    Rule(
        pos_b='adj', pos_a='adv',
        rules=[
            (onlysfx, {'ский', 'цкий', 'ской', 'цкой', 'ий'}),
            (addpfx, {'по-'}),
            (
                [
                    (onlysfx, {'ский', 'цкий', 'ской', 'цкой'}),
                    (delsfx, {'ий', 'ой'}),
                ],
                [
                    (excsfx, {'ский', 'цкий', 'ской', 'цкой'}),
                    (delsfx, {'ий'}),
                    (soft, 'opt'),
                ]
            ),
            (addsfx, {'и'})
        ]
    ),

    # 999
    Rule(
        pos_b='adj', pos_a='adv',
        rules=[
            (addpfx, {'в'}),
            (delsfx, {'ый', 'ой', 'ий'}),
            (addsfx, {'ую'})
	]
    ),

    # 1001
    Rule(
        pos_b='adj', pos_a='adv',
        rules=[
            (excsfx, {'ский', 'цкий'}),
            (addpfx, {'до'}),
            (
                [
                    (delsfx, {'ый', 'ой', 'ий'}),
                    (addsfx, {'а'})
                ],
[
                    (delsfx, {'ий'}),
                    (addsfx, {'я'})
                ],
            )
        ]
    ),

    # 1002

    # 1003
    Rule(
        pos_b='adj', pos_a='adv',
        rules=[
            (excsfx, {'ский', 'цкий'}),
            (
                [
                    (onlypfx, unvoiced),
                    (addpfx, {'ис'}),
                ],
                [
                    (onlypfx, voiced),
                    (addpfx, {'из'}),
                ],
            ),
            (
                [
                    (delsfx, {'ый', 'ой', 'ий'}),
                    (addsfx, {'а'})
                ],
                [
                    (delsfx, {'ий'}),
                    (addsfx, {'я'})
                ],
            )
        ]
    ),

    # 1004
    Rule(
        pos_b='adj', pos_a='adv',
        rules=[
            (onlysfx, {'ый', 'ой'}),
            (addpfx, {'на'}),
            (delsfx, {'ый', 'ой'}),
            (addsfx, {'о'})
        ]
    ),


    # НАРЕЧИЯ, МОТИВИРОВАННЫЕ СУЩЕСТВИТЕЛЬНЫМИ

    # 1009-1010
    Rule(
        pos_b='noun', pos_a='adv',
        rules=[
            (addpfx, {'в', 'на'}),
            (
                [
                    (onlysfx, {'а'}),
                    (delsfx, {'а'}),
                    (addsfx, {'у'})
                ],
                [
                    (excsfx, {'а'}),

                ]
            ),
        ]
    ),


    # НАРЕЧИЯ, МОТИВИРОВАННЫЕ ЧИСЛИТЕЛЬНЫМИ


    # НАРЕЧИЯ, МОТИВИРОВАННЫЕ ГЛАГОЛАМИ

    # 1020
    Rule(
        pos_b='verb', pos_a='adv',
        rules=[
            (delsfx, {'ть'}),
            (
                [
                    (onlysfx, {'ыва', 'ива'}),
                    (delsfx, {'ыва', 'ива'})
                ],
                [
                    (onlysfx, {'а', 'я', 'и'}),
                    (delsfx, {'а', 'я', 'и'}),
                ],
            ),
            (plt, 'try'),
            (addpfx, {'в', 'на'}),
            (addsfx, {'у'})
        ]
    ),

    # НАРЕЧИЯ, МОТИВИРОВАННЫЕ НАРЕЧИЯМИ


    # ПРЕФИКСАЛЬНЫЕ НАРЕЧИЯ С НУЛЕВЫМ СУФФИКСОМ

    # 1024
    Rule(
        pos_b='verb', pos_a='adv',
        rules=[
            (delsfx, {'ть'}),
            (delsfx, {'а', 'я', 'и'}),
            (addpfx, {'в', 'на'}),
            (soft, 'opt')
        ]
    ),

    # add_01
    Rule(
        pos_b='verb', pos_a='adv',
        rules=[
            (onlysfx, {'ать'}),
            (delsfx, {'ть'}),
            (addsfx, {'ючи'}),
        ]
    ),
],


}
