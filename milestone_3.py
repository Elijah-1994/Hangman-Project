
import random

class Hangman:
    
    def __init__ (self,word_list,num_lives=5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guess = "_" * len(self.word)
        self.word_guess = list (self.word_guess)
        self.num_lives = 5
        self.num_letters = set (self.word)
        self.num_letters = list (self.num_letters)
        self.list_of_guesses = []

    def ask_for_input(self):

       while True:
        guess = input ("please enter a single character")
        if len(guess) > 1:
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("you have already tried that letter")
        else:
            self.list_of_guesses.append(guess) 
            return guess    

    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            for i in range (len(self.word)):
                 if guess == str(self.word[i]):
                     print (f"good word {guess} is in the word")
                     self.word_guess[i] = guess
              
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print (f"sorry {guess} is not in the word") 
            print(f"you have {self.num_lives} lives left")

           
           

object_1 = Hangman(['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon'])
object_1.check_guess(object_1.ask_for_input())
 