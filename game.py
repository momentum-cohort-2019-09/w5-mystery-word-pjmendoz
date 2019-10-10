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
    intro = input("Welcome to my game! If you want to play, press 'y', if not, press 'n'.")
    print(intro)

# 4. Grabbing a word from the list that is chosen randomly and finding out the length of the word. Afterwards taking each letter in length of word and replacing it with a blank. 
def get_words(wordlist): 
    random_word = random.choice(wordlist)
    word_length = ([" _ " * len(random_word)])
    print(word_length)
    return random_word    

#5. pushing letters in display
def display_letters(word, correct_guesses):
    display_word = "" 

    for letter in word: 
        if letter in correct_guesses: 
            display_word += letter + " "
        else: 
            display_word += " _ "
    print(display_word)        
   
    
#6. Guessing a letter 
def guess_letter(word, incorrect_guesses, correct_guesses): 
    guessed_letter = input("Guess a letter:")

    # Check if the letter(s) you've guessed are in the word you're guessing    
    if guessed_letter in word: 
        correct_guesses.append(guessed_letter)
        print(f"correct {correct_guesses}")
    else:
        incorrect_guesses.append(guessed_letter)
        print(f"Try again! {incorrect_guesses}") 
    display_letters(word, correct_guesses)   
    return correct_guesses, incorrect_guesses
     

# 7. This is the whole game 
def playing_game(word):
    is_playing = True 
    incorrect_guesses = []
    correct_guesses = []

    while is_playing and len(incorrect_guesses) < 8: 
        guess_letter(word, incorrect_guesses, correct_guesses) 
    print("Game Over!")    

entering_game()
word = get_words(print_my_game("words.txt"))
playing_game(word)


# Read the file -- Done
# Turning words.txt into a list -- Done
# Grabbing random word from lsit -- Done
# Finding out length of random word that was grabbed from list -- Done
# Creating a blank for each letter in the random word -- Done 
# Creating permission to get into game and displaying game -- Done 
# Pushing wrong guesses into a new list stating that the user already chose -- Done
# Pushing right guesses into the display -- Done
# Have a variable that keeps track of my progress -- Done 
# Creating guessing portion of game based on the level that the user chose
# Creating easy, medium and hard mode display
# Determine how many guesses a user can have and minus any that they have lossed due to them guessing wrong answer
# Show you lose or won if user guessed too many times 


