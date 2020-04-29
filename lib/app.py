import random


def RandomNumber():
    # - Pick a random number between 0 and 100
    random_number = random.randrange(0, 100)

    # - Test for random #:
    # print(random_number)

    # - Ask the user to guess the number
    print("Guess our random # between 0-100:")
    guess = int(input())
    print(f"Your guess is {guess}")

    # If the guess is correct, tell the user they guessed correctly and ask if
    # they'd like to play again
    while guess != random_number:
        print(f"{guess} is not correct! It was {random_number}! :(")
        print("Would you like to play again? (Yes or No)")
        play_again = str(input())
        if play_again == "Yes":
            RandomNumber()
        else:
            return print("Goodbye!")
    while guess == random_number:
        print(f"{guess} is correct! :) ")
        print("Would you like to play again? (Yes or No)")
        play_again = str(input())
        if play_again == "Yes":
            RandomNumber()
        else:
            return print("Goodbye!")


RandomNumber()
