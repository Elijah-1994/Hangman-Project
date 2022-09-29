# Hangman-Project
Documenting steps to complete the Hangman Project

Milestone 1 

I have used Python to write the code in milestone 1. This consists of defining a word list of fruits and implementing the import random function to pick a random fruit from the list. The code also includes an ask user input and if/else statement to check if the user input is a single character.

Key things to remember - the len function is required when calculating the length of a string.

Milestone 2

While loop

wrote code that continously ask a user to enter a single character to guess a letter in the word using a while loop. 

Key note = when writting while true you must use a break or return once the condition is true. otherwise the loop will run indefinately.

to check if the guessed word is in the word I had use a for loop within the range of the word and indexing to find if the guessed word is in the word.

For loop/indexing

Key note - remember data type use print(type) to understand the type of data. When you want to itterate a check through a string use indexing. (i.e for i in word if guess = str(word[i])). using indexing will allow you to itteratively check through every letter in the string. 


function

placed the block of code that asks for the user input to guess a chacater in a def ask_input function and the code that checks if the guessed letter is in the word in a def check_letter function.

key note - you can call functions within a function. use return to store the variable and call the function within the function call. (i.e check_guess(ask_for_input())). 

Milestone 3

defined the class using the class syntax. The init method is used to intialise the first instance of the class. The atritbutes are defined by the parameters.
