"""
Кылыг сөзүнүң залогтары

Залог хевири кылдыныгның кымче азы чүже угланганын илередир

Үндезин залог
Кожумак чок

Эгидиишкин залогу
/Кылдыныгның бодунче угланганын илередир/
-н,
-ттын, -ттин, -ттун, -ттүн

Болдуруушкун залогу
/Бир субъектиниң өскезин кылдыныгны кылырынче албадап, дужаап турарын илередир/
-т,
-ттыр, -ттир, -ттур, -ттүр
-зыр, -зир, -зур, -зүр,
-ыр, -ир, -ур, -үр,
-ыс, -ис, -ус, -үс,

Болчуушкун залогу
/Ийи азы оон хөй субъектилерниң удур-дедир, деңге кылган кылдыныын илередир/
-ш,
-ыш, -иш, -уш, -үш
Ш -> т

Качыгдаашкын залогу
/Бир субъектиниң дооразындан бир кылдыныгга алзыпканын илередир/
-л,
-ыл, -ил, -ул, -үл
"""

from general_methods import vowels, consonants, soft_consonants, hard_consonants
from general_methods import word_end1, word_end2, word_end3, word_end4, word_end5
from general_methods import word_end01, word_end02
from general_methods import get_initial_and_is_change


pledge_1_endings = ['']
pledge_2_endings = ['н', 'н', 'н', 'н',
                    'ын', 'ин', 'ун', 'үн',
                    'тын', 'тин', 'тун', 'түн']
pledge_3_endings = ['т', 'т', 'т', 'т',
                    'ыр', 'ир', 'ур', 'үр',
                    'тыр', 'тир', 'тур', 'түр',
                    'зыр', 'зир', 'зур', 'зүр',
                    'ыс', 'ис', 'ус', 'үс']
pledge_4_endings = ['ш', 'ш', 'ш', 'ш',
                    'ыш', 'иш', 'уш', 'үш']
pledge_5_endings = ['л', 'л', 'л', 'л',
                    'ыл', 'ил', 'ул', 'үл']


def set_pledge(word: str, pledge: int) -> str:
    """
    Функция которая на входе получает
    строку и номер залога
    - возвращает строку с окончанием указанного залога
    """
    def set_pledge_0(word: str, endings: list) -> str:
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

    if pledge == 1:
        return word
    if pledge == 2:
        return set_pledge_0(word, pledge_2_endings)
    if pledge == 3:
        return set_pledge_0(word, pledge_3_endings)
    if pledge == 4:
        return set_pledge_0(word, pledge_4_endings)
    if pledge == 5:
        return set_pledge_0(word, pledge_5_endings)

def get_initial_and_case(word: str) -> tuple:
    endings_all = [pledge_1_endings,
                   pledge_2_endings,
                   pledge_3_endings,
                   pledge_4_endings,
                   pledge_5_endings]
    return get_initial_and_is_change(word, endings_all, set_pledge)

if __name__ == '__main__':
    my_list = ['кет', 'маңна', 'бижи', 'чуру', 'эм', 'чугаала', 'бус', 'тып', 'кыл']
    for word in my_list:
        for i in range(1, 6):
            print(set_pledge(word, i), end=', ')
        print()
