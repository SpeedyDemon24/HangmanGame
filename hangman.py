# inputs : total no of gusses allowed 
# random words 
# total no of innorcter gusses
# no of letters gussed correctly 
# length of word

from random_word import RandomWords
import regex
import string
r = RandomWords()

# Return a single random word
word = r.get_random_word()

right_gusses = [0] *len(word)
all_gusses = []
no_of_letters = len(word)
total_no_gusses_allowed = min(no_of_letters*2, 25)
incorrect_guesses = 0 
has_won = False
while incorrect_guesses < total_no_gusses_allowed:
    guess = input("make a guess: ")
    if guess not in list(string.ascii_lowercase):
        print("This is not a lowercase letter or you may have entered more than 1 letter or none")
        continue
    if guess in all_gusses:
        print("This guess has already been made")
        continue 
    all_gusses.append(guess)
    if guess in word:
        indices = [_.start() for _ in regex.finditer(guess, word)]  
        for i in indices:
            right_gusses[i] = 1
        print([letter if right_gusses[i]== 1 else "_" for i, letter  in enumerate(word)])
        if sum(right_gusses) == len(word):
            has_won = True
            
            break
        else:
            print("Correct Guess! Good Job, Keep going!")
    else :
        print("Incorrect Guess, Try Again")
        incorrect_guesses = incorrect_guesses + 1 
if has_won:
    print("You Win")

else:
    print("you have lost the game")
    print(word)




