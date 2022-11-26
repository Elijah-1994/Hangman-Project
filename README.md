# Hangman-Project


The aim of this project is implement the use of python classes to create to the classic hangman game. 

&nbsp;

## Milestone 1 - Create the variables for the game. 
&nbsp;


The first step is to create a list which contains a string of each fruit. The __import random function__ is implemented in order to pick a random word from the list of fruits.  The next step is to implement a __while True loop__ and __if/else__ statements to ask and the player to enter a single character and keep looping looping until the player enters only one character.

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

In order to check if the guessed letter is in the word, the &ensp;__ask_for_input method__&ensp; is placed within the function call of the &ensp;__check_guess method__&ensp; so that 
the guessed letter returned from the &ensp;__ask_for_input method__&ensp; is passed as an argument in the  &ensp;__check_guess method__&ensp;. Within the &ensp;__check_guess method__&ensp;. A for loop is coded to iterate through an index of each letter in the word and if/else statements is coded within the for loop to check if the guessed letter is in the word.

&nbsp;

![Alt text](Project_Images/Milstone%202.PNG)
Figure 2 - Milestone 2 script.

&nbsp;

## Milestone 3 - Create the game class

&nbsp;

In order to code a complete hangman game the use of object orientated programming (OOP) is required.
&nbsp;

__init method__

The init method is used to initialise the first instance of the hangman class. The first argument within the methods in the class will be self. The second argument in the __init method__ is the word_list and the third argument is the __number of lives__ the player has which is set to a default of 5.

The attributes of the class are defined by the parameters. The parameters allow for a complete game loop as they serve multiple purposes such as initialising the starting number of lives and keeping track of the guessed letters. in order the initiate an instance of the class the the class must first be called and then the methods in the class can be called. 

![Alt text](Project_Images/Milstone%203.PNG)
Figure 3 - Milestone 3 script.



&nbsp;


## Milestone 4 - Putting it all together
&nbsp;

__play_game method__

The play game method contains the logic of the game and determines how the game will end.
The logic behind this method is to determine if the user will win or loose the game and how to keep the game loop running until this result is determined.

In order to complete this logic a while loop is coded in this which first check if the number of lives is 0 and if not a elif statement is used to call the __check_guess method__ so that the player can enter another letter. If the number of lives is not 0 and the number of letters is 0 then the player will win the game.