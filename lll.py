import random

class Hangman:
    
    def __init__ (self,word_list,num_lives):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guess = "_" * (self.word)
        self.word_guess = list (self.word_guess)
        self.num_lives = num_lives
        self.num_letters = set (self.word)
        self.num_letters = list (self.num_letters)
        self.list_of_guesses = []


object_1 = Hangman(['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon'],5)