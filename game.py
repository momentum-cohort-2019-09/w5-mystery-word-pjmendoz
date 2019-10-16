import random
import string

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
    permission = input("\n?¿? MYSTERY WORD ?¿? If you want to play, press 'y', if not, press command + d: \n").lower()
    if permission == "y": 
        difficulty_level = input("\nPlease Select Level (e = easy, m = moderate, h = hard):\n").lower()
        if difficulty_level == "e":
            print("\nWelcome to the Easy Level\n")
        if difficulty_level == "m":
            print("\nWelcome to the Moderate Level\n")
        if difficulty_level == "h":
            print("\nWelcome to the Hard Level\n")
    else: 
        print("Please respond with a valid option.")
    return difficulty_level             

# 4. Choosing a level
def level_word(words, difficulty): 
    easy_mode = []
    moderate_mode = []
    hard_mode = []

    for word in words: 
        if len(word) >= 4 and len(word) <=6:
            easy_mode.append(word)
        elif len(word) > 6 and len(word) <=8:
            moderate_mode.append(word)
        elif len(word) > 8: 
            hard_mode.append(word)
    if difficulty == "e":
        index = random.randrange(len(easy_mode) + 1)
        return easy_mode        
    elif difficulty == "m":
        index = random.randrange(len(moderate_mode) + 1)
        return moderate_mode  
    elif difficulty == "h":
        index = random.randrange(len(hard_mode) + 1)
        return hard_mode     

# 5. Grabbing a word from the list that is chosen randomly and finding out the length of the word. Afterwards taking each letter in length of word and replacing it with a blank. 
def get_words(wordlist): 
    random_word = random.choice(wordlist).lower()
    word_length = ([" _ " * len(random_word)])
    print(word_length)
    return random_word    

#6. pushing letters in display
def display_letters(word, correct_guesses):
    display_word = "" 

    for letter in word: 
        if letter in correct_guesses: 
            display_word += letter + " "
        else: 
            display_word += " _ "
    print(display_word)        
   
    
#7. Guessing a letter 
def guess_letter(word, incorrect_guesses, correct_guesses): 
    guessed_letter = input("Guess a letter:")

    # Check if the letter(s) you've guessed are in the word you're guessing  
    if guessed_letter in string.punctuation:
        print("Needs to be a letter")
    elif guessed_letter in " ": 
        print("Needs to be a letter")    
    elif len(guessed_letter) >= 2: 
        print("Needs to be one letter")   
    elif guessed_letter in word: 
        correct_guesses.append(guessed_letter)
        print(f"Correct! {correct_guesses}")
    elif guessed_letter in incorrect_guesses: 
        print("You already guessed that letter. Try again.")
    else:
        incorrect_guesses.append(guessed_letter)
        lives = 8 - len(incorrect_guesses)
        print(f"Wrong answer! Try again!{incorrect_guesses}")
        print(f"You now have {lives} lives left.")
    display_letters(word, correct_guesses)   
    return correct_guesses, incorrect_guesses
     

def player_won(word, correct_guesses):
    for letter in word: 
        if letter not in correct_guesses:
            return False
    return True  

# return all(letter in correct_guesses for letter in word)      

# 8. This is the whole game 
def playing_game():
    is_playing = True 
    incorrect_guesses = []
    correct_guesses = []
    difficulty = entering_game()
    word = get_words(level_word(print_my_game("words.txt"), difficulty))

    while is_playing and len(incorrect_guesses) < 8:
        guess_letter(word, incorrect_guesses, correct_guesses) 
        if player_won(word, correct_guesses): 
            is_playing = False
            print("You won you intellectual bean!") 
    print("Game Over!")    

playing_game()