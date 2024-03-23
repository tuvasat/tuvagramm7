"""
Read.me
"""

# Весь алфавит
alphabet_all = 'АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнҢңОоӨөПпРрСсТтУуYүФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя'
# Гласные
vowels = 'АаЕеЁёИиОоӨөУуYүЫыЭэЮюЯя'
# Мягкие согласные
soft_consonants = 'БбВвГгДдЖжЗзЙйЛлМмНнҢңРр'
# Твердые согласные
hard_consonants = 'КкПпСсТтФфХхЦцЧчШшЩщ'
# Согласные
consonants = 'БбВвГгДдЖжЗзЙйКкЛлМмНнҢңПпРрСсТтФфХхЦцЧчШшЩщ'


# Части речи:
POS_TAGS = [
    'S',            # существительное (яблоня, лошадь, корпус, вечность)
    'A',            # прилагательное (коричневый, таинственный, морской)
    'NUM',          # числительное (четыре, десять, много)
    'A-NUM',        # числительное-прилагательное (один, седьмой, восьмидесятый)
    'V',            # глагол (пользоваться, обрабатывать)
    'ADV',          # наречие (сгоряча, очень)
    'PRAEDIC',      # предикатив (жаль, хорошо, пора)
    'PARENTH',      # вводное слово (кстати, по-моему)
    'S-PRO',        # местоимение-существительное (она, что)
    'A-PRO',        # местоимение-прилагательное (который, твой)
    'ADV-PRO',      # местоименное наречие (где, вот)
    'PRAEDIC-PRO',  # местоимение-предикатив (некого, нечего)
    'PR',           # предлог (под, напротив)
    'CONJ',         # союз (и, чтобы)
    'PART',         # частица (бы, же, пусть)
    'INTJ',         # междометие (увы, батюшки)

    'ANUM',         # XXX: так на самом деле называется 'A-NUM'
    'NONLEX',
]

# Падежи
CASES = frozenset([
    'nom',  # именительный падеж (голова, сын, степь, сани, который)
    'gen',  # родительный падеж (головы, сына, степи, саней, которого)
    'dat',  # дательный падеж (голове, сыну, степи, саням, которому)
    'acc',  # винительный падеж (голову, сына, степь, сани, который/которого)
    'ins',  # творительный падеж (головой, сыном, степью, санями, которым)
    'loc',  # предложный падеж ([о] голове, сыне, степи, санях, котором)
    'gen2',  # второй родительный падеж (чашка чаю)
    'acc2',  # второй винительный падеж (постричься в монахи; по два человека)
    'loc2',  # второй предложный падеж (в лесу, на оси)
    'voc',  # звательная форма (Господи, Серёж, ребят)
    'adnum',  # счётная форма (два часа, три шара)
])

# Адаарының падежи Кым? Чүү? Кымнар? Чүлер?
case_nominative = []

# Хамаарыштырарының падежи Кымның? Чүнүң? Кымнарның? Чүлерниң?
# дүлей болза	            -тың -тиң -туң -түң	        кадаттың эштиң остуң пөштүң
# -л болза	                -дың -диң -дуң -дүң	        талдың элдиң холдуң шөлдүң
# ажык азы -г, -й, -м, -н, -ң, -р болза	    -ның -ниң -нуң -нүң	кажааның черниң номнуң шүүрнүң
case_genitive = ['тың', 'тиң', 'туң', 'түң', 'дың', 'диң', 'дуң', 'дүң', 'ның', 'ниң', 'нуң', 'нүң']

# Бээриниң падежи Кымга? Чүге? Кымнарга? Чүлерге?
# дүлей болза	            -ка -ке	хатка эътке
# ажык болгаш аяар болза	-га -ге	тараага кежигге
case_dative = ['ка', 'ке', 'га', 'ге']

# Онаарының падежи Кымны? Чүнү? Кымнарны? Чүлерни? Чүзүн? Чүлерин?
# Дөстүң сөөлгү үнү	Кожумактың янзылары	Чижектер
# дүлей болза   -ты -ти -ту -тү катты кишти отту уөтү
# -л болза  -ды -ди -ду -дү аалды челди оолду хөлдү
# ажык болгаш аяар болза    -ны -ни -ну -нү торлааны эртемни тонну хүннү
case_accusative = ['ты', 'ти', 'ту', 'тү', 'ды', 'ди', 'ду', 'дү', 'ны', 'ни', 'ну', 'нү']

# Турарының падежи Кымда? Чүде? Кымнарда? Чүлерде?
# Дөстүң сөөлгү үнү	Кожумактың янзылары	Чижектер
# дүлей болза	-та -те	дашта шетте
# ажык азы аяар болза	-да -де	шынаада хүнде
case_local = ['та', 'те', 'да', 'де']

# Үнериниң падежи Кымдан? Чүден? Кымнардан? Чүлерден?
# Дөстүң сөөлгү үнү	Кожумактың янзылары	Чижектер
# дүлей болза	-тан -тен	хаштан эъттен
# ажык азы ыыткыр болза	-дан -ден	оваадан өгден
tuva_original = ['тан', 'тен', 'дан', 'ден']

# Углаарының падежи Кымче? Чүже? Кымнарже? Чүлерже?
# Падежтиң янзызы	Дөстүң сөөлгү үнү	Кожумактың янзылары	Чижектер
# Углаарының 1-ги падежи	дүлей -м, -н, -ң, -л болза	-че	орукче хүнче
# ажык азы -г, -р, й болза	-же	кажааже хоорайже
# Углаарының 2-ги падежи	дүлей болза	-тыва -тиве -тува -түве	шаттыва эштиве хостува көштүве
# ажык азы аяар болза	-дыва -диве -дува -дүве	хадыдыва херимдиве ховудува бөрүдүве
case_directional_1 = ['че', 'же']
case_directional_2 = ['тыва', 'тиве', 'тува', 'түве', 'дыва', 'диве', 'дува', 'дүве']

# Наклонениелер
# Кылдыныгга чугаалап турар кижиниң хамаарылгазын илередир
# кылыг сөзүнүң хевирлерин наклонениелер дээр.
# Болуушкун наклонениези
# Шагда эрткен үе
tuva_nak_shert_chs = ['ган', 'ген', 'кан', 'кен']
tuva_nak_shert_hs = ['нар', 'нер']
tuva_nak_shert_bas = ['баан', 'бээн']


# Одушевленность:
ANIMACY = [
    'anim',  # одушевленность (человек, ангел, утопленник)
    'inan',  # неодушевленность (рука, облако, культура)
]
# Число:
NUMBERS = [
    'sg',  # единственное число (яблоко, гордость)
    'pl',  # множественное число (яблоки, ножницы, детишки)
]

"""
Следующие функции находят на какие звуки
заканчивается слово, от этого зависит какое именно
окончание добавится к слову
"""


def word_end01(word: str, number: int) -> int:
    if word[-number] in 'аыя':  # ы
        return 1
    elif word[-number] in 'еиэ':  # и
        return 2
    elif word[-number] in 'ёоую':  # у
        return 3
    elif word[-number] in 'өү':  # ү
        return 4
    elif word[-number] in 'ъ':  # е
        return word_end02(word, number + 1)


def word_end02(word: str, number: int) -> int:
    if word[- number] in 'аёоуыюя':  # а
        return 1
    elif word[- number] in 'еиөүэ':  # е
        return 2
    elif word[- number] in 'ъ':
        return word_end02(word, number + 1)


"""
Проверка звуков на которые заканчивается слово
для добавления окончания падежа
tuva_un_p = ['тан', 'тен', 'дан', 'ден']
tuva_tu_p = ['та', 'те', 'да', 'де']
"""


def word_end1(word: str) -> (int, None):
    if len(word) < 2:
        return None
    elif word[-1] in hard_consonants:
        return word_end02(word, 2)
    elif word[-1] in soft_consonants:
        return word_end02(word, 2) + 2
    elif word[-1] in vowels:
        return word_end02(word, 1) + 2
    else:
        return None


"""
Проверка звуков на которые заканчивается слово
для добавления окончания падежа
tuva_ha_p = ['дың', 'диң', 'дуң', 'дүң', 'ның', 'ниң', 'нуң', 'нүң', 'тың', 'тиң', 'туң', 'түң']
tuva_on_p = ['ды', 'ди', 'ду', 'дү', 'ны', 'ни', 'ну', 'нү', 'ты', 'ти', 'ту', 'тү']
"""


def word_end2(word: str) -> (int, None):
    if len(word) < 2:
        return None
    elif word[-1] == 'л':
        return word_end01(word, 2)
    elif word[-1] in 'гймнңр':
        return word_end01(word, 2) + 4
    elif word[-1] in vowels:
        return word_end01(word, 1) + 4
    elif word[-1] in consonants:
        return word_end01(word, 2) + 8
    else:
        return None


"""
Проверка звуков на которые заканчивается слово
для добавления окончания падежа 'же', 'че'
"""


def word_end3(word: str) -> (int, None):
    if len(word) < 2:
        return None
    elif word[-1] in (vowels + 'грй'):
        return 1
    elif word[-1] in consonants:
        return 2
    else:
        return None


"""
Проверка звуков на которые заканчивается слово
для добавления окончания падежа 'тыва', 'тиве', 'тува', 'түве', 'дыва', 'диве', 'дува', 'дүве'
"""


def word_end4(word: str) -> (int, None):
    if len(word) < 2:
        return None
    elif word[-1] in hard_consonants:
        return word_end01(word, 2)
    elif word[-1] in soft_consonants:
        return word_end01(word, 2) + 4
    elif word[-1] in vowels:
        return word_end01(word, 1) + 4
    else:
        return None


"""
Проверка звуков на которые заканчивается слово
для добавления окончания множественной формы -лар, -лер, -дар, -дер, -нар, -нер, -тар,-тер
"""


def word_end5(word: str) -> (int, None):
    if len(word) < 2:
        return None
    elif word[-1] in 'грй':
        return word_end02(word, 2)
    elif word[-1] in vowels:
        return word_end02(word, 1)
    elif word[-1] == 'л':
        return word_end02(word, 2) + 2
    elif word[-1] in 'мнц':
        return word_end02(word, 2) + 4
    elif word[-1] in consonants:
        return word_end02(word, 2) + 6
    else:
        return None


def get_initial_and_is_change(word: str, endings_all: dict, set_func) -> tuple:
    for endings_key in endings_all.keys():
        ending_len = len(endings_all[endings_key][0])
        initial_word = word[:-ending_len]
        if ((word[-ending_len:] in endings_all[endings_key]) and
                (word == set_func(initial_word, endings_key))):
            return initial_word, endings_key
    return word, False


def get_letters_not_in_abc(text: str) -> str:
    res = set(text)
    res = ''.join([i for i in res if i not in str(alphabet_all + '-')])
    return res


def get_all_words_from_text(text: str) -> list:
    """
    Функция, которая на входе получает текст и возвращает список.
    Список состоит из всех "слов"
    входящих в текст состоящих из символов тувинского алфавита.
    """
    not_in_abc = get_letters_not_in_abc(text)
    res = text
    for i in not_in_abc:
        res = res.replace(i, ' ')
    res = res.strip().split()
    while True:
        if '-' in res:
            res.remove('-')
        else:
            break
    return res


def get_unique_words_from_text(text: str) -> list:
    """
    Функция, которая на входе получает текст и возвращает список.
    Список состоит из уникальных "слов"
    входящих в текст состоящих из символов тувинского алфавита.
    """
    return sorted(list(set(get_all_words_from_text(text))))
