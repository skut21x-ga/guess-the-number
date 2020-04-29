import random


def RandomNumber():
    # - Pick a random number between 0 and 100
    random_number = random.randrange(0, 100)

    # - Test for random #:
    print(random_number)

    # - Ask the user to guess the number
    print("")
    print(" ------------------------------------------- ")
    print("     ❓ Guess a random # between 0-100: ❓")
    print(" ------------------------------------------- ")
    print("")

    guess = int(input())
    # If the guess is correct, tell the user they guessed correctly and ask if
    # they'd like to play again
    while guess != random_number:
        print("")
        print(" ------------------------------------------ ")
        print(f"    🚨 Your guess '{guess}' is not correct! 🚨")
        print("             Please guess again:")
        print(" ------------------------------------------ ")
        print("")

        guess = int(input())
    while guess == random_number:
        print("")
        print(" ------------------------------------------ ")
        print(f"          🎉  {guess} is correct!  🎉")
        print("       Would you like to play again?")
        print("               (Yes or No)")
        print(" ------------------------------------------")
        print("")
        play_again = str(input())
        if play_again == "Yes":
            RandomNumber()
        else:
            print("")
            print(" ------------------------------------------ ")
            print("         😕 Oh... Okay. Goodbye! 😕")
            print(" ------------------------------------------ ")
            print("")
            exit()


RandomNumber()
