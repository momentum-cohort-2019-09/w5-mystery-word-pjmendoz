import random

# 1. Making words.txt into a list
def my_word_list(words):
    list_of_words = words.split()
    return list_of_words

# 2. Grabbing a word from the list that is chosen randomly and finding out the length of the word

def get_words(wordlist): 
    random_word = random.choice(wordlist)
    word_length = ("_ " * len(random_word))
    print(word_length)
    return random_word

#3. Replacing random word characters as blank spaces "_ "
# def get_blanks(word): 
#     blanks = []
#     word = random_word 
#     for letter in word: 
#         blanks.append(letter.replace("_ ") * word)  
#     return blanks
    

#10. Reads my file
def print_my_game(filename): 
    with open(filename) as file:   
        game = file.read()
        return my_word_list(game)
           
get_words(print_my_game("words.txt"))

# Read the file -- Done
# Turning words.txt into a list -- Done
# Grabbing random word from lsit -- Done
# Finding out length of random word that was grabbed from list -- Done
# Creating a blank for each letter in the random word
# Creating permission to get into game and displaying game if the user says "yes", if no, then return
# Creating easy, medium and hard mode display
# Creating guessing portion of game based on the level that the user chose
# Pushing right guesses into the list of characters needed to create the random word
# Pushing wrong guesses into a new list stating that the user already chose
# Determine how many guesses a user can have
# Show you lose if user guessed too many times 


