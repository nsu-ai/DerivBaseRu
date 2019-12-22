
# DerivBaseRu
A library for building a Russian derivational morphology resourse. It is based on the rules described in "The Russian Grammar" book and includes about 1400 the most productive types of affixational derivation in Russian.

The work on this project is in progress. At the moment, DerivBaseRu allows to derive the possible words from nouns, adjectives, verbs and adverbs.

**TODO**: bug fixing, unittests, resourse building and its visualization.

## Getting Started

### Prerequisites

You should have python3 installed on your machine (we recommend Anaconda3 package) and modules listed in requirements.txt. If you do not have them, run in Terminal

```
pip install -r requirements.txt
```

### Installing and Usage

#### Linux / MacOS
To install this project on your local machine, you should run the following commands in Terminal:

```
git init
git clone https://github.com/nsu-ai/DerivBaseRu.git\
cd DerivBaseRu
```

Examples of using DerivBaseRu:

```
>>> from src.Derivation import Derivation
>>> evaluator = Derivation()

>>> print(evaluator.derive(word_b='красить', pos_b='verb', pos_a='adj'))
['красячий', 'крашливый', 'некрасиемый', 'красильный', 'красливый', 'закрасинный', 'красный', 'закрашенный', 'красительный', 'крашеный', 'красилой', 'краский', 'красьючий', 'красиючий', 'красистый', 'красной', 'красительский', 'краситый', 'бескрасной', 'красилый', 'красинный', 'некрасимый', 'красимый', 'бескрасный', 'некрасный', 'некрасной', 'красивучий', 'крашенный', 'красиемый']

>>> print(evaluator.derive_ext(word_b='красить', pos_b='verb', pos_a='adj'))
[('закраснить', 'rule888(за,и):2'), ('окраснить', 'rule888(за,и):2'), ('украснить', 'rule902(у,и):2'), ('прокраснить', 'rule899(про,и):2'), ('краснничать', 'rule814(нича):1'), ('отокраснить', 'rule894(от,и):2'), ('обкраснить', 'rule888(за,и):2'), ('подокраснить', 'rule896(по,и):1'), ('перекраснить', 'rule895(пере,и):1'), ('отокраснить', 'rule894(от,и):1'), ('подкраснить', 'rule896(по,и):2'), ('скраснить', 'rule899(про,и):2'), ('краснить', 'rule796(и):2'), ('краснничать', 'rule814(нича):2'), ('краснеть', 'rule830(е):3'), ('сокраснить', 'rule899(про,и):2'), ('украснить', 'rule902(у,и):1'), ('обескраснить', 'rule893(обез,и):2'), ('откраснить', 'rule894(от,и):1'), ('перекраснить', 'rule895(пере,и):2'), ('подокраснить', 'rule896(по,и):2'), ('обескраснить', 'rule893(обез,и):1'), ('раскраснить', 'rule900(раз,и):2'), ('покраснить', 'rule896(по,и):1'), ('краснить', 'rule796(и):1'), ('раскраснить', 'rule900(раз,и):1'), ('обокраснить', 'rule888(за,и):2'), ('окраснеть', 'rule905(о,е):2'), ('красовать', 'rule807(ова):1'), ('скраснить', 'rule899(про,и):1'), ('покраснеть', 'rule908(о,е):1'), ('накраснить', 'rule888(за,и):2'), ('сокраснить', 'rule899(про,и):1'), ('красеть', 'rule830(е):1'), ('покраснеть', 'rule908(о,е):2'), ('закраснеть', 'rule904(за,е):1'), ('краснеть', 'rule830(е):1'), ('красствовать', 'rule817(ствова):1'), ('откраснить', 'rule894(от,и):2'), ('прикраснить', 'rule898(при,и):1'), ('подкраснить', 'rule896(по,и):1'), ('искраснить', 'rule889(из,и):1'), ('окраснеть', 'rule905(о,е):1'), ('красниться', 'rule933(и,ся):1'), ('покраснить', 'rule896(по,и):2'), ('прикраснить', 'rule898(при,и):2'), ('красеть', 'rule830(е):2'), ('накраснить', 'rule888(за,и):1'), ('закраснить', 'rule888(за,и):1'), ('окраснить', 'rule888(за,и):1'), ('прокраснить', 'rule899(про,и):1'), ('закраснеть', 'rule904(за,е):2'), ('искраснить', 'rule889(из,и):2'), ('обокраснить', 'rule888(за,и):1'), ('красновать', 'rule807(ова):1'), ('обкраснить', 'rule888(за,и):1'), ('красновать', 'rule807(ова):2'), ('красниться', 'rule933(и,ся):2')]

```

## Running the tests

To run the automated tests for this system (may take some time), use a command

```
python test.py
```

## Contributing
...

## Authors

* **Daniil Vodolazsky** - [s231644](https://github.com/s231644)

See also the list of [contributors](https://github.com/nsu-ai/DerivBaseRu/contributors) who participated in this project.

## License
...


## Acknowledgments
...

## Publications
...