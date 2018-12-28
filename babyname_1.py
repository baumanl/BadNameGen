import string
import random


def getletter(inpt):
    if len(inpt) > 1:
        print('enter a valid input')
    elif inpt == 'V':
        return random.choice(vowels)
    elif inpt == 'C':
        return random.choice(consonants)
    elif input == '_':
        return random.choice(string.ascii_lowercase)
    else:
        return inpt


def generator():
    letter1 = getletter(l1_in)
    letter2 = getletter(l2_in)
    letter3 = getletter(l3_in)
    letter4 = getletter(l4_in)
    letter5 = getletter(l5_in)
    name = letter1+letter2+letter3+letter4+letter5
    return name


l1_in = input('Letter1: Choose option:..."V" for vowel, "C" for consonant, "_" for do not care, or desired (lowercase)')
l2_in = input('Letter2: Choose option:..."V" for vowel, "C" for consonant, "_" for do not care, or desired (lowercase)')
l3_in = input('Letter3: Choose option:..."V" for vowel, "C" for consonant, "_" for do not care, or desired (lowercase)')
l4_in = input('Letter4: Choose option:..."V" for vowel, "C" for consonant, "_" for do not care, or desired (lowercase)')
l5_in = input('Letter5: Choose option:..."V" for vowel, "C" for consonant, "_" for do not care, or desired (lowercase)')

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

for i in range(20):
    print(generator())
