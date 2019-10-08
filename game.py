import random

# making words.txt into a list
def my_word_list(words):
    list_of_words = words.split()
    return list_of_words

#grabbing a word from the list that is chosen randomly
def get_words(wordlist): 
    random_word = random.choice(wordlist)
    print(random_word)
    return random_word

# reads my file
def print_my_game(filename): 
    with open(filename) as file:   
        game = file.read()
        return my_word_list(game)
           
get_words(print_my_game("words.txt"))


