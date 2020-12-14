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