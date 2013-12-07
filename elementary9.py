#!/usr/bin/python
#
# Write a guessing game where the user has to guess a secret number. After every
# guess the program tells the user whether his number was too large or too
# small. At the end the number of tries needed should be printed. I counts only
# as one try if the user inputs the same number consecutively.

from random import randint

secret = randint(1, 1000)
guess = -1
guesses = set()

while guess != secret:
    print("Please guess a number between 0 and 1000: ", end="")
    guess = int(input())
    if guess != secret:
        print("Wrong! ", end="")
        guesses.add(guess)
    if guess < secret:
        print("Correct answer is larger.")
    else:
        print("Correct answer is smaller.")
print("Correct! ", end="")
print("You guessed {0!s} times.".format(len(guesses)))
