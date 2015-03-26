__author__ = 'w.acheson'
import nltk
#nltk.download() # to download more corpas, such as the cmudict!

from nltk.corpus import cmudict

cmu = (cmudict.dict())
vowels = ['A', 'E', 'I', 'O' ,'U']

def cmu_entry(word = ''):
    arpabet = ''

    for x in cmu[word.lower()]:
        arpabet = x

    if len(arpabet) > 0:
        print arpabet
        return arpabet
    else:
        return word + ' not found'

def syl_comp(arpabet):
    syl_notes = ''
    print arpabet
    for count, phoneme in enumerate(arpabet):
        #print phoneme + ' count ' + str(count)
        for char_count, char in enumerate(phoneme):
            #print "=== char " +  char + ' char_count ' + str(char_count)
            if any(char in vow for vow in vowels) == True:
                print char
                syl_notes += '.'
                break
    return syl_notes


print syl_comp(cmu_entry("amygdala"))