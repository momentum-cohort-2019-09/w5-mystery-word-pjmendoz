import random

# 1. making words.txt into a list
def my_word_list(words):
    list_of_words = words.split()
    return list_of_words

# 2. grabbing a word from the list that is chosen randomly
def get_words(wordlist): 
    random_word = random.choice(wordlist)
    word_length = len(random_word)
    print(random_word)
    print(word_length)
    return random_word

# reads my file
def print_my_game(filename): 
    with open(filename) as file:   
        game = file.read()
        return my_word_list(game)
           
get_words(print_my_game("words.txt"))

# read list
# make a list of words from words.txt
# grab random word
# figuring out the length of each word


