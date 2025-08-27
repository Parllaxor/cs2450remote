# Program that tries to guess your age

import random
import sys

name = input("""Hello! What is your name? """)
print(f"""Hello {name}, nice to meet you!
I'd like to guess how old you are.""")

def guess_age(name):
    guessed_numbers = []
    x = 1
    while x > 0:
        random_age = random.randint(15, 30)
        if random_age not in guessed_numbers:
            age_guess = input(f"Are you {random_age} years old? ")
            if "y" in age_guess.lower():
                print(f"""YES! {name} is {random_age} years old!""")
                sys.exit()

            elif "n" in age_guess.lower():
                print("""Rats.""")
                guessed_numbers.append(random_age)

            else:
                print("""I don't understand that, let me try guessing again.""")

guess_age(name)