
import re
from collections import defaultdict
from operator import itemgetter


"""Open the file and try reading the data"""
try:
    file_name = input('Input the file name: ')
except:
    print('This input is invalid! Please try again.')
    exit()
try:
    file = open(file_name,"r")
except FileNotFoundError:
    print('Error. File cannot be opened:', file_name)
    exit()


"function to define dictionary so words will be processed"
word_dictionary = defaultdict(int)
word_count = 0
letters_dictionary = defaultdict(int)
regex = re.compile('([^\s\w]|[0-9_])')

for line in file:
    line = line.rstrip()
    try:
        line = regex.sub('', line)
        line = line.lower()
        words = line.split()
        for word in words:
            print(word)
            word_dictionary[word] += 1
            word_count = word_count + 1
            for letter in word:
                print(letter)
                letters_dictionary[letter] += 1
    except:
        print('Data was unreadable. Try another file.')
        exit()

if len(word_dictionary) == 0:
    print('No words are present in the file. Try another file')
    exit()

"To print total number of words"
print(f'The are {word_count} total words.')

"To calculate total number of distnict words"
distinct_words = len(word_dictionary.items())

"To print total number of distnict words"
print(f'The are {distinct_words} distinct words.')

"to calculate top 25 most used words"
sorted_words = sorted(word_dictionary.items(),key=itemgetter(1), reverse=True)
top_words = sorted_words[:25]

"To print top used words"
print('The top 25 most used words are:')
for key, value in top_words:
    print(f'{key} : {(value)}')

letters = sorted(letters_dictionary.items(),key=itemgetter(1), reverse=True)

"To print top used letters"
print('The top most used letters are:')
for key, value in letters:
    print(f'{key} : {(value)}')
