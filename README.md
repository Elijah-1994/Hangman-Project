# Hangman-Project


The aim of this project is to implement the use of python class and methods to create to the classic hangman game. 

&nbsp;

## Milestone 1 - Create the variables for the game. 
&nbsp;


The first step is to create a list which contains a string of each fruit. The &ensp;__import random function__&ensp; is implemented in order to pick a random word from the list of fruits.  The next step is to implement a __while True loop__ and __if/else__ statements to ask and the player to enter a single character and to keep looping until the player enters only one character.

&nbsp;

![Alt text](Project_Images/Milstone%201.PNG)
Figure 1 - Milestone 1 script.

&nbsp;
## Milestone 2 - Check if the guessed character is in the word.
&nbsp;

__ask_for_input method__
&nbsp;

The code written in milestone 1 was encapsulated into the &ensp;__ask_for_input method__&ensp; and returns the guessed letter in string format.

&nbsp;

__check_guess method__

In order to check if the guessed letter is in the word,the &ensp;__ask_for_input method__&ensp; is placed within the function call of the &ensp;__check_guess method__&ensp; so that 
the guessed letter returned from the &ensp;__ask_for_input method__&ensp; is passed as an argument in the  &ensp;__check_guess method__&ensp;. Within the &ensp;__check_guess method__&ensp;, a for loop is coded to iterate through an index of each letter in the word and if/else statements is coded within the for loop to check if the guessed letter is in the word.

&nbsp;

![Alt text](Project_Images/Milstone%202.PNG)
Figure 2 - Milestone 2 script.

&nbsp;

## Milestone 3 - Create the game class

&nbsp;

In order to code a complete hangman game the use of object orientated programming (OOP) is required.
&nbsp;

__init method__

The init method is used to initialise the first instance of the Hangman Class. The first argument within the method is self. The second argument in the __init method__ is the word_list and the third argument is the __number of lives__ the player has which is set to a default of 5.

The attributes of the class are defined by the parameters. Each parameter is assigned as  self.name as a variable name. This is to ensure that the script does not throw out a positional arguments error. The parameters within the __init method__ allow for a complete game loop as they serve multiple purposes such as initialising the starting number of lives and keeping track of the guessed letters. The full list of parameter are below:

* Self.word_list: The list of words in the game.
* Self.word: The word chosen randomly from the list of words.
* Self.word_guess: The chosen word hidden in "_" string to be guessed by the player.
* Self.num_lives: The starting number of lives.
* Self.num_letters: Contains the number of unique letters chosen by the player.
* Self.list_of_guesses: List of the unique letters guessed by the player.

in order the initiate an instance of the class the the class must first be called and then the methods within in the class can be called. 


![Alt text](Project_Images/Milstone%203.PNG)
Figure 3 - Milestone 3 script.



&nbsp;


## Milestone 4 - Putting it all together
&nbsp;


__check_guess method__
&nbsp;

The advantage of OOP is that the parameters within __init method__ can be updated as a global variable. To take advantage of this within the __check_guess method__  the self.num_letters parameter is coded to decrease by 1 each time a correct letter is guessed and the self.num_lives parameter is coded to decrease by 1 each time an incorrect letter is guessed.
&nbsp;


__play_game method__

The play game method contains the logic of the game and determines how the game will end.
The logic behind this method is to determine if the user will win or loose the game and to keep the game loop running until this result is determined.

In order to complete this logic a while loop is coded which first checks if the number of lives is 0 which means the user looses and the loop is broken. If not then an elif statement is used to call the __check_guess method__ so that the player can enter another letter. If the number of lives is not 0 and the number of letters is 0 then the player will win the game and the while loop will break. Since parameters initialised in the __init__ method are only the first instance of the class, the parameters are only defined within the __init__ method and cannot be called in other methods. In order to call the methods in the class and check the parameters within the __play_game method__ the function and parameter calls should start with game.method or parameter.

