"""
Produce a list of the most frequent interesting words, along with a summary
table showing where those words appear (sentences and documents)
"""

import os
from collections import Counter
import pprint # enables print of notes to user. displays txt files too

# Note to user on purpose of this app
def print_notes():
    star = '*'.center(80, '*')
    print(star)
    message = 'Select document number, from 1 to 6'
    print('*' + message.center(78) + '*')
    message = 'Today, we can find the 10 most common words used.'
    print('*' + message.center(78) + '*')
    message = 'All returned words sourced from this apps directory.'
    print('*' + message.center(78) + '*')
    print(star + '\n') # New line

"""
Get txt file method prints all the txt files from the directory, based upon
the document option selected by the user.
"""

def get_txt_file():
    count = 0 # To count txt files in directory
    text_files = [] # List created to hold txt files in directory 
    file_dict = {}
    
    """
    Iterate through all files in directory to find .txt files.
    """
    
    for foldername, subfolders, filenames in os.walk(os.getcwd()):
        for file in filenames:
            if file[-4:] == '.txt':
                print(str(count + 1) + '.' +file) # number & name of each file
                text_files.append(file) # adds selected file to the list
                count += 1 # count of files

    if count == 0: # If no txt files found, start again & find files
        print("No files were found in the directory. Program to exit.")
        exit()
        
    """
    Get users txt document choice
    """
    
    while True:
        try:
            # User invited to select a document number
            selected_file = int(input("Please enter a number from the list: "))
            if selected_file <= 0:
                raise IndexError
            filename = str(text_files[selected_file - 1])
            break
        except ValueError:
            print("Invalid number - Please try again.") # Error message.
        except IndexError:
            print('Number choice out of range, please select between 1 and' + str(count)) # Error message
            
        document = open(filename, encoding="utf8") # Open selected document
        content = document.read() # File text assigned to content
        document.close() # Document closed when no longer viewed
        document_string = str(content) # Document content assigned to string, then split string
        
        return document_string
        
        """
        Dictionary for all words contained in txt documents & frequency used.
        """
        
        def document_dictionary(document):
            # Key value pair | Key = word | Value = word frequency
            result = {}
            for item in document.split():
                if item not in result:
                    result[item] = 1
                else:
                    result[item] += 1
                    
            return result
            
        """
        Dictionary for 128 common words to be viewed on/off from table reports.  
        """
        
        def document_dictionary_uncommon(document):
            common_words = {"a", "about", "after", "all", "also", "an", "and",
                            "any", "are", "as", "at", "back", "be", "because",
                            "been", "being", "but", "by", "can", "change",
                            "come", "could", "day", "do", "dont", "even",
                            "first", "for", "from", "get", "give", "go",
                            "good", "had", "has", "have", "he", "her", "here", 
                            "him", "his", "how", "i", "if", "in", "into",
                            "is", "it", "its", "just", "keep", "know", "let", 
                            "lets", "like", "look", "make", "many", "me",
                            "more", "most", "mr", "mrs", "my", "need", "new", 
                            "no", "not", "now", "of", "on", "one", "only",
                            "or", "other", "our", "out", "over", "own", "part", 
                            "person", "push", "say", "said", "see", "she", 
                            "so", "some", "take", "than", "that", "thats",
                            "the", "their", "them", "then", "there", "these",
                            "they", "think", "this", "those", "time", "to",
                            "two", "up", "us", "use", "wait", "was", "way", 
                            "we", "well", "were", "weve", "what", "when",
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
            
        """
        Print table to be viewed by the user.
        """
        
        def print_table(title, dict):
            star = '*'.center(80, '*') # To mark out rows of the table
            print(star)
            
            print('*' + title.center(78) + '*') # Table title
            print(star)
            
            print('*' + "Common Words".center(25) +
                  '*' + "Frequency".center(25) +
                  '*' + "% of Document".center(26) + '*') # Column headings
            print(star)
            
            # Loop through dictionary to print word, frequency & % value too.
            for key, value in dict.items():
                print('*' + key.center(25) +
                      '*' + str(value).center(25) +
                      '*' + (str('{0:.2f}' .format(value / total_words)) + '%'
                      .center(26) + '*'))
                print(star)
                
                print("\n") # Spacer between tables 
                
        """
        Main variables defined.
        """
        
        While True:
            # ** Instructions to user **
            print_instructions()
            # ** Get document selected by user **
            document = get_txt_file()
            # ** For words & word frequency **
            words_count = document_dictionary(document)
            # ** For words & word frequency, in lower case ** 
            words_count_lower = document_dictionary(document.lower())
            # ** Check words and remove 128 common words, re dictionary ** 
            words_count_uncommon = document_dictionary_uncommon
                                   (document.lower())
            # ** Document total word count ** 
            total_words = sum(words_count.values())
            # ** Dictionary inc top 10 words from document **
            top_words = dict(Counter(words_count).most_common(10))
            # ** Dictionary inc top 10 words from document, lower case **
            top_words_lower = dict(Counter(words_count_lower).most_common(10))
            # ** Dictionary inc top 10 uncommon words from document, lower case
            top_uncommon_words_lower = dict(Counter(words_count_uncommon)
                                            .most_common(10))