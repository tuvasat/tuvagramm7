"""
Модуль, который позволяет разделить тувинские слова на слоги.
Формат:
- на вход мы получаем слово строчными буквами
- на выходе мы подаем слово разбитые на слоги слово

силернии-биле
си~~лер~~нии-~би~~ле
"""

from general_methods import vowels, consonants
import general_methods


def get_syllabled_word(word: str) -> str:
    """
    Расставляем символы мягкого переноса слова
    Например: кижилер -> ки~жи~лер
    :param word:
    :return:
    """

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

        istroka = ''
        for i in word:
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

    def slog(sg_form: str, word_form: str) -> str:
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

    res = []
    res0 = []
    if '-' in word:
        res0 = word.split('-')
    for word0 in res0:
        res.append(get_syllabled_word0(word0))
    return '-~'.join(res)

print(12345)
print(__name__)
if __name__ == '__main__':
    print(12345)
    pass
