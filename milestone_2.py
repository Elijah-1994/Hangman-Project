import random

word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']

word_list = random.choice(word_list)

def ask_for_input():

    while True:
         guess = input ("please enter a single character")
         if len(guess) == 1:
           break
         else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    if len(guess) == 1:
        return guess

    
    
def check_guess(guess):
    guess = guess.lower()
    for i in range (len(word_list)):
        if guess == str(word_list[i]):
         print (f"good word {guess} is in the word")
         break
    
        else:
            print (f"sorry {guess} is not in the word. please try again")
            break

    
check_guess(ask_for_input())    