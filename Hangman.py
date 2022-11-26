#%%
import random
#%%
class Hangman:
    '''
        This class represents the game loop for the hangman game. 
        
        Attributes:
            self.word_list: The list of words in the game.
            self.word: The word chosen randomly from the list of words.
            self.word_guess: The chosen word hidden in "_" string to be guessed by the player.
            self.num_lives: The starting number of lives.
            self.num_letters: Contains the number of unique letters chosen by the player.
            self.list_of_guesses: List of the unique letters guessed by the player.
    
    '''
    
    def __init__ (self,word_list,num_lives=5):
        '''
        See help(Hangman) for accurate signature
        
        '''
        self.word_list = word_list
        self.word = random.choice(self.word_list)
        self.word_guess = "_" * len(self.word)
        self.word_guess = list (self.word_guess)
        self.num_lives = 5
        self.num_letters = set (self.word)
        self.num_letters = len (self.num_letters)
        self.list_of_guesses = []
    pass

    def ask_for_input(self)->str:
       '''
        This method asks the player for a single letter and checks if the letter has already been guessed. If the letter has been guessed the player must enter 
        another letter.
        
        Returns:
            str: returns the guessed letter. 
        
        '''   
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
        '''
        This method  checks if the letter entered by the player is in the word. If the guessed letter is not in the word,
        the player will loose 1 life.
        
        Arguments: guessed letter.
        
        '''   
        guess = guess.lower()
        if guess in self.word:
            for i in range (len(self.word)):
                 if guess == str(self.word[i]):
                     print (f"good guess, {guess} is in the word")
                     self.word_guess[i] = guess
              
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print (f"sorry {guess} is not in the word") 
            print(f"you have {self.num_lives} lives left")
              
    pass     

def play_game():
    '''
        This method is used to end the game. If the number of lives is 0, the player looses the game. If not the method will call the
        player the guess another letter. If the number of lives is not 0 and the number of letters is 0, the player wins the game.
        
    '''   
    game = Hangman(word_list,num_lives=5)
    
    while True:
        if game.num_lives == 0:
            print ("you lost!")
            break
        
        elif game.num_letters > 0:
            game.check_guess(game.ask_for_input())
        
        elif game.num_lives != 0 and game.num_letters == 0:
            print ("congratulations you won the game")
            break

    pass

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon'] 
    play_game() 