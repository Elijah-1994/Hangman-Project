guess = input("please enter a single letter")

if guess == 1:
    print ("Good guess")
    
else:
    print("Ooops! that is not a valid input")



import random

word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']

word_list = random.choice(word_list)

print (word_list)