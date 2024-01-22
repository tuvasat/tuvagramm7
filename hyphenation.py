"""
Модуль, который позволяет разделить тувинские слова на слоги.
Формат:
- на вход мы получаем слово строчными буквами
- на выходе мы подаем слово разбитые на слоги слово

силернии-биле
си~~лер~~нии-~би~~ле
"""

from tuvagramm import vowels, consonants


def sgsg(slovo: str) -> str:
    """
    Формирование шаблона слова по типам символов
    g - гласные
    s - согласные
    z - ьъ
    :param slovo:
    :return:
    """
    mtz = {'ъ', 'ь'}
    dfs = '-'

    istroka = ''
    for i in slovo:
        if i in vowels:
            istroka = istroka + 'g'
        elif i in consonants:
            istroka = istroka + 's'
        elif i == dfs:
            istroka = istroka + '-'
        elif i in mtz:
            istroka = istroka + 'z'
        else:
            break
    return istroka


def slog(islog, iline):
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
    #slog0 = {'sg-', 'gs-', 'gsg-', 'sgg-', 'sgs-', 'sggs-', 'gsgs-', 'gsggs-', 'ggsg-', 'ggs-',
    #         'sgss-', 'ssg-', 'gsggs-', 'gzs-', 'gggs-'}
    # --------------------------------------------

    if (islog[:4] in slog2) or (islog[:5] in slog2) or (islog[:6] in slog2):
        iline = iline[:2] + '~' + iline[2:]
    elif (islog[:5] in slog3) or (islog[:6] in slog3) or (islog[:7] in slog3):
        iline = iline[0:3] + '~' + iline[3:]
    elif (islog[:5] in slog4) or (islog[:6] in slog4) or (islog[:7] in slog4) or (islog[:8] in slog4):
        iline = iline[0:4] + '~' + iline[4:]
    elif (islog[:7] in slog5) or (islog[:8] in slog5) or (islog[:9] in slog5) or (islog[:10] in slog5):
        iline = iline[0:5] + '~' + iline[5:]
    elif (islog[:8] in slog6) or (islog[:9] in slog6) or (islog[:10] in slog6):
        iline = iline[0:6] + '~' + iline[6:]
#    elif (islog[:3] in slog0) or (islog[:4] in slog0) or (islog[:5] in slog0) \
#            or (islog[:6] in slog0) or (islog[:6] in slog0):
#        iline = iline[0:islog.index('-') + 1] + '~' + iline[islog.index('-') + 1:]
    else:
        iline = ''
    return iline

def get_syllabled_word(word: str) -> str:
    """
    Расставляем символы мягкого переноса слова
    Например: кижилер -> ки~жи~лер
    :param word:
    :return:
    """

    res = []
    res0 = []
    if '-' in word:
        res0 = word.split('-')
    for word0 in res0:
        res.append(get_syllabled_word0(word0))
    return '-~'.join(res)


def get_syllabled_word0(word: str) -> str:
    """
    Расставляем символы мягкого переноса слова
    Например: кижилер -> ки~жи~лер
    :param word: str
    :return: str
    """
    word0 = word
    # Вызываем функцию формирование шаблона слова по видам символов
    template = sgsg(word0)
    syllable = word0
    word0 = ''
    while len(template) > 1:
        if (slog(template, syllable)) == '':
            break
        else:
            syllable = (slog(template, syllable))
            word0 += '~~' + syllable.split('~')[0]
            syllable = syllable.split('~')[1]
            template = sgsg(syllable)
    word0 = word0[2:] + '~~' + syllable.split('~')[0]
    return word0

def main():
    print(get_syllabled_word('силернии-биле'))


if __name__ == '__main__':
    main()
