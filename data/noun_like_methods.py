"""
Этот модуль представляет собой сборник классов и функций
для работы с существительными.
Нахождение существительных в тексте.
Преобразование существительных.
Преобразование других частей речи в существительные.
"""

from general_methods import vowels, consonants, soft_consonants, hard_consonants
from general_methods import word_end1, word_end2, word_end3, word_end4, word_end5
from general_methods import word_end01, word_end02
from general_methods import get_initial_and_is_change


"""
Адаарының падежи Кым? Чүү? Кымнар? Чүлер?
------------------------------------------
Бээриниң падежи Кымга? Чүге? Кымнарга? Чүлерге?
Дөстүң сөөлгү үнү	Кожумактың янзылары	Чижектер
дүлей болза	-ка -ке	хатка эътке
ажык болгаш аяар болза	-га -ге	тараага кежигге
------------------------------------------
Турарының падежи Кымда? Чүде? Кымнарда? Чүлерде?
Дөстүң сөөлгү үнү	Кожумактың янзылары	Чижектер
дүлей болза	-та -те	дашта шетте
ажык азы аяар болза	-да -де	шынаада хүнде
------------------------------------------
Үнериниң падежи Кымдан? Чүден? Кымнардан? Чүлерден?
Дөстүң сөөлгү үнү	Кожумактың янзылары	Чижектер
дүлей болза	-тан -тен	хаштан эъттен
ажык азы ыыткыр болза	-дан -ден	оваадан өгден
------------------------------------------
Хамаарыштырарының падежи Кымның? Чүнүң? Кымнарның? Чүлерниң?
Дөстүң сөөлгү үнү	Кожумактың янзылары	Чижектер
дүлей болза	-тың -тиң -туң -түң	кадаттың эштиң остуң пөштүң
-л болза	-дың -диң -дуң -дүң	талдың элдиң холдуң шөлдүң
ажык азы -г, -й, -м, -н, -ң, -р болза	-ның -ниң -нуң -нүң	кажааның черниң номнуң шүүрнүң
------------------------------------------
Онаарының падежи Кымны? Чүнү? Кымнарны? Чүлерни? Чүзүн? Чүлерин?
Дөстүң сөөлгү үнү	Кожумактың янзылары	Чижектер
дүлей болза   -ты -ти -ту -тү катты кишти отту уөтү
-л болза  -ды -ди -ду -дү аалды челди оолду хөлдү
ажык болгаш аяар болза    -ны -ни -ну -нү торлааны эртемни тонну хүннү
------------------------------------------
Углаарының падежи Кымче? Чүже? Кымнарже? Чүлерже?
Углаарының 1-ги падежи	дүлей -м, -н, -ң, -л болза	-че	орукче хүнче
ажык азы -г, -р, й болза	-же	кажааже хоорайже
------------------------------------------
Углаарының падежи Кымче? Чүже? Кымнарже? Чүлерже?
Углаарының 2-ги падежи	дүлей болза	-тыва -тиве -тува -түве	шаттыва эштиве хостува көштүве
ажык азы аяар болза	-дыва -диве -дува -дүве	хадыдыва херимдиве ховудува бөрүдүве
"""


# Окончания падежей
case_endings_nominative_1 = ['']
case_endings_genitive_12 = ['дың', 'диң', 'дуң', 'дүң',
                            'ның', 'ниң', 'нуң', 'нүң',
                            'тың', 'тиң', 'туң', 'түң']
case_endings_genitive_22 = ['дыы', 'дии', 'дуу', 'дүү',
                            'ныы', 'нии', 'нуу', 'нүү',
                            'тыы', 'тии', 'туу', 'түү']
case_endings_dative_3 = ['ка', 'ке', 'га', 'ге']
case_endings_accusative_4 = ['ды', 'ди', 'ду', 'дү',
                             'ны', 'ни', 'ну', 'нү',
                             'ты', 'ти', 'ту', 'тү']
case_endings_local_5 = ['та', 'те', 'да', 'де']
case_endings_original_6 = ['тан', 'тен', 'дан', 'ден']
case_endings_directional_17 = ['же', 'че']
case_endings_directional_27 = ['тыва', 'тиве', 'тува', 'түве',
                               'дыва', 'диве', 'дува', 'дүве']
case_endings_all = {1: case_endings_nominative_1,
                    12: case_endings_genitive_12,
                    22: case_endings_genitive_22,
                    3: case_endings_dative_3,
                    4: case_endings_accusative_4,
                    5: case_endings_local_5,
                    6: case_endings_original_6,
                    17: case_endings_directional_17,
                    27: case_endings_directional_27}


def set_case(word: str, case: int) -> str:
    """
    Функция которая на входе получает
    строку и номер падежа
    - возвращает строку с окончанием указанного падежа
    (В тувинском языке всего 7 падежей, 7-й падеж имеет 2 разных формы.
    Эти формы пронумерованы как 71 и 72)
    """
    if case == 1:
        return word
    elif case == 2:
        return word + case_endings_genitive_12[word_end2(word) - 1]
    elif case == 12:
        return word + case_endings_genitive_12[word_end2(word) - 1]
    elif case == 22:
        return word + case_endings_genitive_22[word_end2(word) - 1]
    elif case == 3:
        return word + case_endings_dative_3[word_end1(word) - 1]
    elif case == 4:
        return word + case_endings_accusative_4[word_end2(word) - 1]
    elif case == 5:
        return word + case_endings_local_5[word_end1(word) - 1]
    elif case == 6:
        return word + case_endings_original_6[word_end1(word) - 1]
    elif case == 7:
        return word + case_endings_directional_17[word_end3(word) - 1]
    elif case == 17:
        return word + case_endings_directional_17[word_end3(word) - 1]
    elif case == 27:
        return word + case_endings_directional_27[word_end4(word) - 1]


def get_initial_and_case(word: str) -> tuple:
    return get_initial_and_is_change(word, case_endings_all, set_case)


def is_case(word: str) -> bool:
    _, res = get_initial_and_is_change(word, case_endings_all, set_case)
    return res


# окончания множественной формы существительных
endings_plural_form = ['лар', 'лер', 'дар', 'дер',
                       'нар', 'нер', 'тар', 'тер']
endings_plural_all = {1: endings_plural_form}


def set_plural(word: str, form=1) -> str:
    """
    Класс который на входе получает существительное в единственном числе
    - возвращает существительное во множественном числе
    :param word:
    :return:
    """
    return word + endings_plural_form[word_end5(word) - 1]


def get_initial_and_is_plural(word: str) -> tuple:
    return get_initial_and_is_change(word, endings_plural_all, set_plural)


def is_plural(word: str) -> bool:
    _, res = get_initial_and_is_change(word, endings_plural_all, set_plural)
    return res


endings_possessive_1 = ['м', 'м', 'м', 'м', 'ым', 'им', 'ум', 'үм']
endings_possessive_2 = ['ң', 'ң', 'ң', 'ң', 'ың', 'иң', 'уң', 'үң']
endings_possessive_3 = ['зы', 'зи', 'зу', 'зү', 'ы', 'и', 'у', 'ү']
endings_possessive_all = {1: endings_possessive_1,
                          2: endings_possessive_2,
                          3: endings_possessive_3}


def set_possessive(word: str, form: int) -> str:
    """
    Функция которая на входе получает существительное и номер притяжательной формы
    - возвращает существительное притяжательной формы
    :param word:
    :param form:
    :return:
    """
    def set_possessive_0(word: str, endings: list) -> str:
        if word[-1] in vowels:
            return word + endings[word_end01(word, 1) - 1]
        elif word[-1] in soft_consonants:
            return word + endings[word_end01(word, 2) + 3]
        elif word[-1] in hard_consonants:
            if word[-1] in 'т':
                word = word[:-1] + 'д'
            elif word[-1] in 'п':
                word = word[:-1] + 'в'
            return word + endings[word_end01(word, 2) + 3]

    if form == 1:
        return set_possessive_0(word, endings_possessive_1)
    if form == 2:
        return set_possessive_0(word, endings_possessive_2)
    if form == 3:
        return set_possessive_0(word, endings_possessive_3)


def get_initial_and_possessive(word: str) -> tuple:
    return get_initial_and_is_change(word,
                                     endings_possessive_all,
                                     set_possessive)


def is_possessive(word: str) -> bool:
    _, res = get_initial_and_is_change(word,
                                       endings_possessive_all,
                                       set_possessive)
    return res


def get_initial_words_in_text(text: str) -> dict:
    def filter_word():
        pass

    res = dict()
    from general_methods import get_unique_words_from_text
#    punctuation_marks = get_punctuation_marks(text)
    words = get_unique_words_from_text(text.lower())
    words0 = sorted(list(set(words)))
    while words0:
        word0 = words0.pop(0)
        if len(word0) > 3 and word0 not in ' '.join(res.values()):
            for word in words0.copy():
                if word0 in word:
                    try:
                        res[word0] + ' ' + word
                    except:
                        res[word0] = word
                    words0.remove(word)
    return res


if __name__ == '__main__':
    print(is_case('кижиnfg'))
#    with open('text/text.txt', 'r', encoding='utf-8') as f1:
#        print(get_words_in_text(' '.join(f1.readlines())))
