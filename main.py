import random
import os

# function that takes
Words = ["hello", "word", "bring", "search", "take", "succeed", "play", "work", "failure", "work", "me"]

'''
Here we use a list to make it easier for the player to guess.
We could also use files to make the experience more random.
'''
computer_choice = random.choice(Words)  # computer chooses the word
inputs = list()  # variable used in the main loop to store user inputs
attempts = 10

# display function
def display(*args):
    size = len(args)  # variable to store the size
    choice = str(args[0])  # word chosen by the computer
    if size == 0:
        return IndexError
    if size == 1:
        for i in range(0, len(choice)):
            print("_ ", end="")
    if size > 1:
        letters = []
        for n in range(1, size):
            letters.append(args[n])
        for i in range(0, len(choice)):
            if choice[i] in letters:
                print(choice[i], end="")
            else:
                print("_ ", end="")

# function that checks if the user has won
def victory(word: list, letters):
    count = 0
    for i in word:
        if i in set(letters):
            count += 1
    if count == len(word):
        return True
    return False

# function to check if the letter is found
def found(word, char):
    if char in word:
        return True
    return 0

inputs.append(computer_choice)
display(computer_choice)

os.system("clear")

# Main loop
while victory(computer_choice, set(inputs)) == False:
    letter = str(input("\n Enter a letter: "))  # get user input
    if found(computer_choice, letter):
        inputs.append(letter)
    else:
        attempts -= 1
    if attempts <= 0:
        print("\n The word was \"" + computer_choice + "\"")
        break
    os.system("clear")
    display(*inputs)

if victory(computer_choice, set(inputs)):
    print("\n$*************************** YOU WIN ***************************$")
else:
    print("\n$*************************** YOU LOSE ***************************$")
