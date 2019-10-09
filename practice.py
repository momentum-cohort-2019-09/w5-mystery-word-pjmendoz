import random

def my_word_list(words):
    list_of_words = words.split()
    return list_of_words

def get_words(wordlist): 
    random_word = random.choice(wordlist)
    word_length = ("_ " * len(random_word))
    print(word_length)
    return random_word
    
def print_my_game(filename): 
    with open(filename) as file:   
        game = file.read()
        return my_word_list(game)
           
get_words(print_my_game("words.txt"))
