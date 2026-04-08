# Project 2 — Number Guessing Game
# Author: Şevval Özlü

import random

difficulty = input("Choose difficulty: (1) Easy 1-10 (2) Medium 1-50 (3) Hard 1-100:)

                   if difficulty == "1":
                      max_number = 10
                  elif difficulty == "2":
                      max_number = 50
                  else:
                      max_number = 100
# TODO: generate a random secret number between 1 and 10
secret = random.randint(1, max_number)

# TODO: set up a guesses counter
guesses = 0

# TODO: get the user's first guess
guess = int(input(f"Guess a number between 1 and {max_number}: "))

# TODO: while loop — keep asking until the guess is correct
while guess != secret:
      guesses += 1

      if guess < secret:
        print("Too low!")
      else:
        print("Too high!")

      guess = int(input(f"Try again (1-{max_number}): "))
#   - print "Too low!" or "Too high!" on each wrong guess
#   - count each guess
# TODO: print the congratulations message with the number of guesses
guesses += 1
print(f"Correct! You got it in {guesses} guesses.")
