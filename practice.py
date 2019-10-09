import random

# making words.txt into a list
def my_word_list(words):
    list_of_words = words.split()
    return list_of_words

#grabbing a word from the list that is chosen randomly and finding out the length of the word
def get_words(wordlist): 
    random_word = random.choice(wordlist)
    return random_word

def length_of_word(random_word):
    word_length = len(random_word)
    print(word_length)
    return word_length

# reads my file and is my main function
def print_my_game(filename): 
    with open(filename) as file:   
        game = file.read()
        return my_word_list(game)
           
get_(print_my_game("words.txt"))
