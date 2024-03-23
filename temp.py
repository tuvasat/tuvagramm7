from data.general_methods import *
from data.hyphenation import *
"""
with open('txt/text.txt', 'r', encoding='utf-8') as f:
    words = get_unique_words_from_text(''.join(f.readline()))
    for word in words:
        print(word)
        print(get_syllable_word(word))
"""

print(get_syllable_word('хөөрежир-улустар-хамаарыштыр-дыр'))

