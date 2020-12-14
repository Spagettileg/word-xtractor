"""
Produce a list of the most frequent interesting words, along with a summary
table showing where those words appear (sentences and documents)
"""

import os
from collections import Counter
import pprint  # enables print of notes to user. displays txt files too


def print_notes():
    '''
    Note to user on purpose of this app
    '''
    star = '*'.center(78, '*')
    print(star)
    message = 'Select document number, from 1 to 6'
    print('*' + message.center(76) + '*')
    message = 'Today, we can find the 10 most common words used.'
    print('*' + message.center(76) + '*')
    message = 'All returned words sourced from this apps directory.'
    print('*' + message.center(76) + '*')
    print(star + '\n')  # New line


'''
Get txt file method prints all the txt files from the directory, based upon
the document option selected by the user.
'''


def get_txt_file():
    # To count txt files in directory
    count = 0  # To count txt files in directory
    # List created to hold txt files in directory
    text_files = []
    file_dict = {}
    # Iterate through all files in directory to find .txt files.
    for folderName, subfolders, filenames in os.walk(os.getcwd()):
        for file in filenames:
            # find the files ending in .txt
            if file[-4:] == '.txt':
                # number & name of each file
                print(str(count + 1) + '. ' + file)
                # adds selected file to the list
                text_files.append(file)
                # count of files
                count += 1

    # If no txt files found, start again & find files
    if count == 0:
        print("No files were found in the working folder. The program will now exit.")
        exit()

    # Get users txt document choice
    while True:
        try:
            # User invited to select a document number
            selected_file = int(input("Please enter a number from the list: "))
            # raise IndexError if the users input is less than or equal to zero
            if selected_file <= 0:
                raise IndexError
            # extract that file from the list
            filename = str(text_files[selected_file - 1])
            break
        except ValueError:
            # Error message
            print("That was not a valid number.  Try again...")
        except IndexError:
            # Error message
            print('That value was out of range.  please select between 1 and ' + str(count))

    # open selected document
    document = open(filename, encoding="utf8")
    # file text assigned to content
    content = document.read()
    # document closed when no longer viewed
    document.close()
    # document content assigned to string, then split string
    document_string = str(content)
    
    return document_string


'''
Dictionary for all words contained in txt documents & frequency used.
'''


def document_dictionary(document):
    # Key value pair | Key = word | Value = word frequency
    result = {}
    for item in document.split():
        if item not in result:
            result[item] = 1
        else:
            result[item] += 1

    return result


'''
dictionary for 128 common words to be viewed on/off from table reports.
'''
def document_dictionary_uncommon(document):
    common_words = {"a", "about", "after", "all", "also", "an", "and",
                "any", "are", "as", "at", "back", "be", "because",
                "been", "being", "but", "by", "can", "change",
                "come", "could", "day", "do", "don't", "even",
                "first", "for", "from", "get", "give", "go",
                "good", "had", "has", "have", "he", "her", "here",
                "him", "his", "how", "i", "if", "in", "into",
                "is", "it", "it's", "its",  "just", "keep", "know", "let",
                "let's", "like", "look", "make", "many", "me",
                "more", "most", "mr", "mrs", "my", "need", "new",
                "no", "not", "now", "of", "on", "one", "only",
                "or", "other", "our", "out", "over", "own", "part",
                "person", "push", "say", "said", "see", "she",
                "so", "some", "take", "than", "that", "that's",
                "the", "their", "them", "then", "there", "these",
                "they", "think", "this", "those", "time", "to",
                "two", "up", "us", "use", "wait", "was", "way",
                "we", "well", "we'll", "were", "we've", "what", "when",
                "where", "which", "who", "why", "will", "with",
                "work", "would", "year", "you", "your"}


    # Dictionary created. Key = word. Value = word frequency
    result = {}
    for item in document.split():
        if item not in common_words:
            if item not in result:
                result[item] = 1
            else:
                result[item] += 1

    return result

''' print table to be viewed by the user. '''

def print_table(title, dict):
    # To mark out rows of the table
    star = '*'.center(80, '*')
    print(star)

    # table title
    print('*' + title.center(78) + '*')
    print(star)

    # column headings
    print('*' + "Most Common Words".center(25) + '*' + "Times Appeared".center(25) + '*' +
          "Percentage of Book".center(26) + '*')
    print(star)

    # Loop through dictionary to print word, frequency & % value too.
    for key, value in dict.items():
        print('*' + key.center(25) + '*' + str(value).center(25) + '*' +
              (str('{0:.2f}'.format(value / total_words)) + '%').center(26) + '*')
        print(star)

    # spacer between tables.
    print("\n")

''' main variables defined. '''
while True:
    # notes to user 
    print_notes()

    # get document selected by user 
    document = get_txt_file()

    # for words & word frequency 
    words_count = document_dictionary(document)

    # for words & word frequency, in lower case 
    words_count_lower = document_dictionary(document.lower())

    # check words and remove 128 common words, re dictionary, in lower case 
    words_count_uncommon = document_dictionary_uncommon(document.lower())

    # document total word count 
    total_words = sum(words_count.values())

    # dictionary inc top 10 words from document 
    top_words = dict(Counter(words_count).most_common(10))

    # dictionary inc top 10 words from document, lower case 
    top_words_lower = dict(Counter(words_count_lower).most_common(10))

    # Dictionary inc top 10 uncommon words from document, lower case
    top_uncommon_words_lower = dict(Counter(words_count_uncommon).most_common(10))

    # ***************************
    # *** printing the tables ***
    # ***************************
    title = "Top 10 words used (inc upper & lower case)"
    print_table(title, top_words)

    title = "Top 10 words used (all text in lower case)"
    print_table(title, top_words_lower)

    title = "Top 10 words used (lower case, less common words)"
    print_table(title, top_uncommon_words_lower)

    # *************************************************
    # ** chance for user to review another document. **
    # *************************************************
    while True:
        print('Review another document?  Y/N')
        do_again = str(input())
        if do_again.upper() == 'N':
            exit()
        elif do_again.upper() != 'Y':
            print('Please enter Y or N')
        else:
            break
