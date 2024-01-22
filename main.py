import tuvagramm
from tuvagramm import alphabet_all
from difflib import SequenceMatcher


PUNCTUATION_MARKS = ':^,«»]•.- \t[!_/)?№*\n;('


def get_punctuation_marks(line: str) -> str:
    res = ''
    for i in line:
        if i not in alphabet_all and not i.isalnum():
            res += i
    res = ''.join(set(res))
    return res


def line_to_words(line: str) -> list:
    res = ''
    for i in line:
        if i not in PUNCTUATION_MARKS and not i.isdigit():
            res += i
        else:
            res += ' '
    res = res.split()
    return res


def get_endings(path='sim_words.txt') -> set:
    res = set()
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.split()
            ending_begin = len(line[0])
            for word in line[1:]:
                print(word[ending_begin:])

                res.add(word[ending_begin:])
    return res


def get_sim_words(words: list) -> list:
    res = []
    sorted(words, key=len)

    with open('sim_words.txt', 'a', encoding='utf-8') as f:
        for word1 in words:
            pre = []
            for word2 in words:
                if (word1 != word2) and (len(word1) > 1) and (word1 in word2):
                    if pre == []:
                        pre.append(word1)
                    pre.append(word2)
            if pre:
                res = res + pre
                f.write(' '.join(pre) + '\n')
    return res


def finde_nouns(path='sim_words.txt') -> dict:
    res = dict()
    noun_endings = ['лар', 'лер', 'дар', 'дер', 'нар', 'нер', 'тар', 'тер',
                    'дың', 'диң', 'дуң', 'дүң', 'ның', 'ниң', 'нуң', 'нүң', 'тың', 'тиң', 'туң', 'түң',
                    'ка', 'ке', 'га', 'ге',
                    'ды', 'ди', 'ду', 'дү', 'ны', 'ни', 'ну', 'нү', 'ты', 'ти', 'ту', 'тү',
                    'та', 'те', 'да', 'де',
                    'тан', 'тен', 'дан', 'ден',
                    'же', 'че',
                    'тыва', 'тиве', 'тува', 'түве', 'дыва', 'диве', 'дува', 'дүве',
                    'м', 'м', 'м', 'м', 'ым', 'им', 'ум', 'үм',
                    'ң', 'ң', 'ң', 'ң', 'ың', 'иң', 'уң', 'үң',
                    'зы', 'зи', 'зу', 'зү', 'ы', 'и', 'у', 'ү',
                    ]
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.split()

            ending_begin = len(line[0])
            line_endings = []

            for word in line[1:]:
                print(word, word[ending_begin:])
    return res

def gt(words):

    for word1 in words:
        for word2 in words:
            if word1 != word2:
                if SequenceMatcher(None, word1, word2).ratio() > 0.9:
                    print(word1, word2)


if __name__ == '__main__':
    """
    with open('text/text1.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    lines = ' '.join(lines)
    words = line_to_words(lines)
    words = ' '.join(set(words)).lower().split()
    """

    #print(get_sim_words(words))
    #print(get_endings())
    """
    with open('endings.txt', 'w', encoding='utf-8') as f:
        f.write(' '.join(get_endings()))
    """

    finde_nouns()
