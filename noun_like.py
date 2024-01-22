"""
Этот модуль представляет собой сборник классов и функций
для работы с существительными.
Нахождение существительных в тексте.
Преобразование существительных.
Преобразование других частей речи в существительные.
"""

from tuvagramm import vowels, consonants, soft_consonants, hard_consonants
from tuvagramm import word_end1, word_end2, word_end3, word_end4, word_end5
from tuvagramm import word_end01, word_end02
from tuvagramm import get_initial_and_is_change


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
case_endings_ad_1 = ['']
case_endings_ha_2 = ['дың', 'диң', 'дуң', 'дүң', 'ның', 'ниң', 'нуң', 'нүң', 'тың', 'тиң', 'туң', 'түң']
case_endings_be_3 = ['ка', 'ке', 'га', 'ге']
case_endings_on_4 = ['ды', 'ди', 'ду', 'дү', 'ны', 'ни', 'ну', 'нү', 'ты', 'ти', 'ту', 'тү']
case_endings_tu_5 = ['та', 'те', 'да', 'де']
case_endings_un_6 = ['тан', 'тен', 'дан', 'ден']
case_endings_ug_17 = ['же', 'че']
case_endings_ug_27 = ['тыва', 'тиве', 'тува', 'түве', 'дыва', 'диве', 'дува', 'дүве']


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
        return word + case_endings_ha_2[word_end2(word) - 1]
    elif case == 3:
        return word + case_endings_be_3[word_end1(word) - 1]
    elif case == 4:
        return word + case_endings_on_4[word_end2(word) - 1]
    elif case == 5:
        return word + case_endings_tu_5[word_end1(word) - 1]
    elif case == 6:
        return word + case_endings_un_6[word_end1(word) - 1]
    elif case == 7:
        return word + case_endings_ug_17[word_end3(word) - 1]
    elif case == 17:
        return word + case_endings_ug_17[word_end3(word) - 1]
    elif case == 27:
        return word + case_endings_ug_27[word_end4(word) - 1]


def get_initial_and_case(word: str) -> tuple:
    endings_all = [case_endings_ad_1,
                   case_endings_ha_2,
                   case_endings_be_3,
                   case_endings_on_4,
                   case_endings_tu_5,
                   case_endings_un_6,
                   case_endings_ug_17,
                   case_endings_ug_27]
    return get_initial_and_is_change(word, endings_all, set_case)


# окончания множественной формы существительных
endings_plural_form = ['лар', 'лер', 'дар', 'дер', 'нар', 'нер', 'тар', 'тер']


def set_plural(word: str, form=1) -> str:
    """
    Класс который на входе получает существительное в единственном числе
    - возвращает существительное во множественном числе
    :param word:
    :return:
    """
    return word + endings_plural_form[word_end5(word) - 1]


def get_initial_and_is_plural(word: str) -> tuple:
    endings_all = [endings_plural_form]
    return get_initial_and_is_change(word, endings_all, set_plural)


endings_possessive_1 = ['м', 'м', 'м', 'м', 'ым', 'им', 'ум', 'үм']
endings_possessive_2 = ['ң', 'ң', 'ң', 'ң', 'ың', 'иң', 'уң', 'үң']
endings_possessive_3 = ['зы', 'зи', 'зу', 'зү', 'ы', 'и', 'у', 'ү']


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
    endings_all = [endings_possessive_1,
                   endings_possessive_2,
                   endings_possessive_3
                   ]
    return get_initial_and_is_change(word, endings_all, set_possessive)


# Окончания количественных числительных
endings_quantitative_numeral = ['кы', 'ки', 'ку', 'кү', 'гы', 'ги', 'гу', 'гү']


if __name__ == '__main__':
    print(get_initial_and_possessive('кижиң'))
