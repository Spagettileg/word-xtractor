"""
Produce a list of the most frequent interesting words, along with a summary
table showing where those words appear (sentences and documents)
"""

import os
from collections import Counter
import pprint # enables print of notes to user. displays txt files too

def print_notes():
    # Note to user on purpose of this app
    
    star = '*'.center(80, '*')
    print(star)
    message = 'Select document number, from 1 to 6'
    print('*' + message.center(78) + '*')
    message = 'Today, we can find the 10 most common words used.'
    print('*' + message.center(78) + '*')
    message = 'All returned words sourced from this apps directory.'
    print('*' + message.center(78) + '*')
    print(star + '\n') # New line
    