import random

# 1. Reads my file
def print_my_game(filename): 
    with open(filename) as file:   
        game = file.read()
        return my_word_list(game)

# 2. Making words.txt into a list
def my_word_list(words):
    list_of_words = words.split()
    return list_of_words

# 3. Entering Game
def entering_game():
    intro = input("Welcome to my game! If you want to play, press 'enter'.")
    print(intro)

# 4. Grabbing a word from the list that is chosen randomly and finding out the length of the word. Afterwards taking each letter in length of word and replacing it with a blank. 
def get_words(wordlist): 
    random_word = random.choice(wordlist)
    word_length = (["_ " * len(random_word)])
    print(word_length)
    return random_word    

#5 Guessing a letter 
def guess_letter(word, incorrect_guesses, correct_guesses): 
    guessed_letter = input("To play, guess a random letter that maybe part of the random word that was selected by the computer:")

    # Check if the letter(s) you've guessed are in the word you're guessing    
    if guessed_letter in word: 
        correct_guesses.append(guessed_letter)
        print(f"These are my correct guesses {correct_guesses}")
    else:
        incorrect_guesses.append(guessed_letter)
        print(f"These are incorrect guesses {incorrect_guesses}")     

# 5. This is the whole game 
def playing_game(word):
    is_playing = True 
    incorrect_guesses = []
    correct_guesses = []

    while is_playing and len(incorrect_guesses) < 8: 
        guess_letter(word, incorrect_guesses, correct_guesses) 
    
  
entering_game()
word = get_words(print_my_game("words.txt"))  
playing_game(word)

# Read the file -- Done
# Turning words.txt into a list -- Done
# Grabbing random word from lsit -- Done
# Finding out length of random word that was grabbed from list -- Done
# Creating a blank for each letter in the random word -- Done 
# Creating permission to get into game and displaying game -- Done 
# Pushing right guesses into the list of characters needed to create the random word -- Done
# Pushing wrong guesses into a new list stating that the user already chose -- Done

# Creating guessing portion of game based on the level that the user chose
# Creating easy, medium and hard mode display
# Determine how many guesses a user can have
# Show you lose or won if user guessed too many times 


