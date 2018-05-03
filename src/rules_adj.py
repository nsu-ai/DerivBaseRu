from src.functions import *

rules_adj = [
    # 611
    Rule(
        pos_b='noun', pos_a='adj',
        rules=[
            (
                [
                    (onlysfx, {'ь', 'й'}),
                    (delsfx, 'opt', {'ь'}),
                    (delvowel, 'opt'),
                    (addsfx, {'ев'})
                ],
                [
                    (onlysfx, consonants),
                    (addsfx, {'ов'})
                ],
            )
        ]
    ),

    # 612
    Rule(
        pos_b='noun', pos_a='adj',
        rules=[
                (onlysfx, {'а', 'я'}),
                (delsfx, {'а', 'я'}),
                (
                    [
                        (onlysfx, {'ц'}),
                        (addsfx, {'ын'})
                    ],
                    [
                        (excsfx, {'ц'}),
                        (addsfx, {'ин'})
                    ],
                )
        ]
    ),


    Rule(
        pos_b='noun', pos_a='adj',
        rules=[
            (
                [
                    (onlysfx, {'а', 'ь'}),
                    (delsfx, {'а', 'ь'}),
                ],
                [
                    (excsfx, {'а', 'ь'}),
                ],
            ),
            (plt, 'try'),
            (addvowel, 'opt'),
            (addsfx, {'ий'})
        ]
    ),

    # 616
    Rule(
        pos_b='noun', pos_a='adj',
        rules=[
            (
                [
                    (onlysfx, {'я', 'а', 'ь'}),
                    (delsfx, {'я', 'а', 'ь'}),
                ],
                [
                    (excsfx, {'я', 'а', 'ь'}),
                    (replsfx, {('ей', 'ь')}),
                ],
            ),
            (plt, 'try'),
            (delvowel, 'opt'),
            (addsfx, {'иный'})
        ]
    ),

    # 619
    Rule(
        pos_b='noun', pos_a='adj',
        rules=[
            (excsfx, {'тель', 'ист', 'ние', 'ация', 'ция'}),
            (delsfx, 'try', {'о', 'а', 'ь', 'ие', 'ий'}),
            (plt, 'try'),
            (addsfx, {'ный', 'ной'})
        ]
    ),

    Rule(
        pos_b='noun', pos_a='adj',
        rules=[
            (excsfx, {'тель', 'ист', 'ние', 'ация', 'ция'}),
            (delsfx, {'о', 'а', 'ь', 'ие', 'ий', 'ия'}),
            (addsfx, {'енный'})
        ]
    ),

    Rule(
        pos_b='noun', pos_a='adj',
        rules=[
            (onlysfx, {'ия'}),
            (delsfx, {'а', 'я'}),
            (addsfx, {'онный'})
        ]
    ),

    Rule(
        pos_b='noun', pos_a='adj',
        rules=[
            (delsfx, 'try', {'о', 'а', 'ь', 'я', 'ы', 'ие', 'ий', 'ия', 'ус', 'юс', 'ум'}),
            (onlysfx, paired | velar | vowels),
            (addsfx, {'озный', 'альный', 'арный'})
        ]
    ),

    Rule(
        pos_b='noun', pos_a='adj',
        rules=[
            (delsfx, 'try', {'о', 'а', 'ь', 'ия', 'я', 'ы', 'ие', 'ий', 'ия', 'ус', 'юс', 'ум'}),
            (onlysfx, {'д', 'т', 'з', 'с'}),
            (addsfx, {'орный', 'уальный', 'ивный'})
        ]
    ),

    Rule(
        pos_b='noun', pos_a='adj',
        rules=[
            (delsfx, 'try', {'о', 'а', 'ь', 'ия', 'я', 'ы', 'ие', 'ий', 'ия'}),
            (onlysfx, paired | velar),
            (addsfx, {'ичный', 'иальный'})
        ]
    ),

    Rule(
        pos_b='noun', pos_a='adj',
        rules=[
            (delsfx, {'ние'}),
            (replsfx, 'try', {('е', 'и')}),
            (addsfx, {'тельный'})
        ]
    ),

    # 626
    Rule(
        pos_b='noun', pos_a='adj',
        rules=[
            (delsfx, 'try', {'ация', 'а'}),
            (addsfx, {'абельный'})
        ]
    ),

    # 628
    Rule(
        pos_b='noun', pos_a='adj',
        rules=[
            (delsfx, 'try', {'я', 'а', 'ь', 'й', 'и', 'о', 'е'}),
            (delvowel, 'opt'),
            (addsfx, {'овый', 'евый'})
        ]
    ),

    # 630
    Rule(
        pos_b='noun', pos_a='adj',
        rules=[
            (delsfx, 'try', {'я', 'а', 'ь', 'й', 'и', 'о', 'е'}),
            (plt, 'try'),
            (delvowel, 'opt'),
            (addsfx, {'ский', 'ской', 'еский', 'овский', 'овской', 'евский'})
        ]
    ),

    # 632
    Rule(
        pos_b='noun', pos_a='adj',
        rules=[
            (delsfx, 'try', {'я', 'а', 'ь', 'й', 'и', 'о', 'е', 'ы'}),
            (plt, 'try'),
            (delvowel, 'opt'),
            (addsfx, {'анский', 'инский', 'ийский', 'ческий', 'ический'})
        ]
    ),

    # 636
    Rule(
        pos_b='noun', pos_a='adj',
        rules=[
            (delsfx, 'try', {'я', 'а', 'ь', 'й', 'и', 'о', 'е', 'ы'}),
            (addsfx, {'ианский'})
        ]
    ),

    # 637
    Rule(
        pos_b='noun', pos_a='adj',
        rules=[
            (delsfx, 'try', {'я', 'а', 'ь', 'й', 'и', 'о', 'е', 'ы'}),
            (addsfx, {'астый', 'ястый'})
        ]
    ),

    # 638
    Rule(
        pos_b='noun', pos_a='adj',
        rules=[
            (delsfx, 'try', {'я', 'а', 'ь', 'й', 'и', 'о', 'е', 'ы'}),
            (addsfx, {'атый'})
        ]
    ),

    # 639
    Rule(
        pos_b='noun', pos_a='adj',
        rules=[
            (delsfx, 'try', {'я', 'а', 'ь', 'й', 'и', 'о', 'е', 'ы'}),
            (addsfx, {'чатый'})
        ]
    ),

    # 640
    Rule(
        pos_b='noun', pos_a='adj',
        rules=[
            (delsfx, 'try', {'я', 'а', 'ь', 'й', 'и', 'о', 'е', 'ы'}),
            (addsfx, {'оватый', 'еватый'})
        ]
    ),

    # 641
    Rule(
        pos_b='noun', pos_a='adj',
        rules=[
            (delsfx, 'try', {'я', 'а', 'ь', 'й', 'и', 'о', 'е', 'ы'}),
            (addsfx, {'овитый', 'евитый'})
        ]
    ),

    # 642
    Rule(
        pos_b='noun', pos_a='adj',
        rules=[
            (delsfx, 'try', {'я', 'а', 'ь', 'й', 'и', 'о', 'е', 'ы'}),
            (addsfx, {'истый'})
        ]
    ),

    # 643
    Rule(
        pos_b='noun', pos_a='adj',
        rules=[
            (delsfx, 'try', {'я', 'а', 'ь', 'й', 'и', 'о', 'е', 'ы'}),
            (addsfx, {'ливый'})
        ]
    ),










]
