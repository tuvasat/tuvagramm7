"""
Модуль, который позволяет разделить тувинские слова на слоги.
Формат:
- на вход мы получаем слово строчными буквами
- на выходе мы подаем слово разбитые на слоги слово

силернии-биле
си~~лер~~нии-~би~~ле
"""

import json
import os.path
from data.general_methods import vowels, consonants


def sgsg(word: str) -> str:
    """
    Формирование шаблона слова по типам символов
    g - гласные
    s - согласные
    z - ьъ
    :param word:
    :return:
    """
    mtz = {'ъ', 'ь'}
    dfs = '-'

    res = ''
    for i in word:
        if i in vowels:
            res = res + 'g'
        elif i in consonants:
            res = res + 's'
        elif i == dfs:
            res = res + '-'
        elif i in mtz:
            res = res + 'z'
        else:
            break
    return res


def slog0(sg_form: str, word_form: str) -> str:
    """
    расставляем символы мягкого переноса
    :param islog:
    :param iline:
    :return:
    """
    # Шаблоны слогов
    slog2 = {'gssg', 'sgsg', 'gssgg', 'sgszg'}
    slog3 = {'gzssgs', 'ggssg', 'sggsg', 'sgssg', 'sggsg', 'sgsgs', 'gsssg', 'gsgsg', 'ssgsg'}
    slog4 = {'ggsgsg', 'sggssg', 'gsgssg', 'gsggsg', 'ssgssg', 'sgsssg', 'ggsgsgs', 'sgszsg', 'sgszsg', 'ggszsg'}
    slog5 = {'ggsggsg', 'gsggssg', 'sggsssgs', 'sggsssgs', 'gsgsssg', 'sgssssg', 'ggsgssg', 'ssgsssg',
             'gszgssg', 'sgsszsg'}
    slog6 = {'ggsggssg'}

    if (sg_form[:4] in slog2) or (sg_form[:5] in slog2) or (sg_form[:6] in slog2):
        word_form = word_form[:2] + '~' + word_form[2:]
    elif (sg_form[:5] in slog3) or (sg_form[:6] in slog3) or (sg_form[:7] in slog3):
        word_form = word_form[0:3] + '~' + word_form[3:]
    elif (sg_form[:5] in slog4) or (sg_form[:6] in slog4) or (sg_form[:7] in slog4) or (sg_form[:8] in slog4):
        word_form = word_form[0:4] + '~' + word_form[4:]
    elif (sg_form[:7] in slog5) or (sg_form[:8] in slog5) or (sg_form[:9] in slog5) or (sg_form[:10] in slog5):
        word_form = word_form[0:5] + '~' + word_form[5:]
    elif (sg_form[:8] in slog6) or (sg_form[:9] in slog6) or (sg_form[:10] in slog6):
        word_form = word_form[0:6] + '~' + word_form[6:]
    else:
        word_form = ''
    return word_form


ggsggssg = {"2": "gssg sgsg gssgg sgszg",
            "3": "gzssgs ggssg sggsg sgssg sggsg sgsgs gsssg gsgsg ssgsg",
            "4": "ggsgsg sggssg gsgssg gsggsg ssgssg sgsssg ggsgsgs sgszsg sgszsg ggszsg",
            "5": "ggsggsg gsggssg sggsssgs sggsssgs gsgsssg sgssssg ggsgssg ssgsssg gszgssg sgsszsg",
            "6": "ggsggssg"
            }


def get_syllables(template: str, word: str) -> str:
    with open('data/hyphenation_tamplates.json', 'r', encoding='utf-8') as f:
        s = f.read()
    h_tamplate = json.loads(s)

    flag = False
    for key in h_tamplate.keys():
        key = int(key)
        for template_len in range(key, len(template)):
            if template[:template_len] in h_tamplate[str(key)].split():
                word = word[:key] + '~' + word[key:]
                flag = True
                break
        if flag:
            break
    return word


def get_syllable_word0(word: str) -> str:
    """
    Расставляем символы мягкого переноса слова
    Например: кижилер -> ки~жи~лер
    :param word: str
    :return: str
    """
    # Вызываем функцию формирование шаблона слова по видам символов
    template = sgsg(word)
    syllable = word
    res = ''
    while len(template) > 1:
        syllables = get_syllables(template, syllable)
        if syllables.split('~') == '' or len(syllables.split('~')) < 2:
            break
        else:
            syllable = syllables
            res += '~~' + syllable.split('~')[0]
            if len(syllable.split('~')) > 1:
                syllable = syllable.split('~')[1]
                template = sgsg(syllable)
    res = res[2:] + '~~' + syllable.split('~')[0]
    return res


def get_syllable_word(word: str) -> str:
    """
    Расставляем символы мягкого переноса слова
    Например: кижилер -> ки~жи~лер
    :param word:
    :return:
    """
    res = []
    res0 = word.split('-')
    for word0 in res0:
        res.append(get_syllable_word0(word0))
    return '-~'.join(res)


def set_syllable_template(syllable_word: str, sign='~', file_path='data/hyphenation_tamplates0.json') -> str:
    """
    Функция принимает слово с мягкими переносами и
    формирует по нему шаблон расстановки мягких переносов
    :param syllable_word: слово с мягкими переносами
    :param sign: знак разделитель, по умолчанию '~'
    :param file_path: файл сохранения по умолчанию 'data/hyphenation_tamplates0.json'
    :return: шаблон переноса в строковом виде
    """
    h_template = dict()
    for word_part0 in syllable_word.split('-'):
        word_part = []
        for syllable in word_part0.split('~'):
            if syllable:
                word_part.append(sgsg(syllable))

        while len(word_part) > 2:
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    h_template = json.loads(f.read())
            else:
                h_template = json.dumps(dict())
                with open(file_path, 'w', encoding='utf-8') as f:
                    json.dump(h_template, file_path)

                with open(file_path, 'r', encoding='utf-8') as f:
                    h_template = json.loads(f.read())

            new_template = word_part[0] + word_part[1]
            key = len(word_part[0])
            try:
                print(word_part[0])
                value = ' '.join(sorted(list(set(f'{h_template[f"{len(word_part[0])}"]} {new_template}'.split()))))
            except:
                value = new_template
            print(12345, key, value)
            print(type(h_template), h_template)
            h_template[str(key)] = str(value)

            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(h_template, f, indent=4)

            word_part.pop(0)
    return h_template
