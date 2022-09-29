import random

class Hangman:
    
    def __init__ (self,word_list,num_lives=5):
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guess = "_" * len(self.word)
        self.word_guess = list (self.word_guess)
        self.num_lives = 5
        self.num_letters = set (self.word)
        self.num_letters = len (self.num_letters)
        self.list_of_guesses = []
    pass
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
    pass
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
    
        while self.num_lives == 0:
            print ("you lost!")
        
        while self.num_letters > 0:
            return
        
        while self.num_lives > 0 and self.num_letters == 0:
            print ("congratulations you won the game")
            return
              
    pass     

def play_game():
    game = Hangman(word_list,num_lives=5)
    game.check_guess(game.ask_for_input())
    game.check_guess(game.ask_for_input())
    game.check_guess(game.ask_for_input())
    game.check_guess(game.ask_for_input())
    game.check_guess(game.ask_for_input())
    game.check_guess(game.ask_for_input())
    game.check_guess(game.ask_for_input())
    game.check_guess(game.ask_for_input())  
    pass

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon'] 
    play_game() 