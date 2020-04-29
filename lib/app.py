import random


def RandomNumber():
    random_number = random.randrange(0, 100)
    # test for random #:
    # print(random_number)
    print("What do you think the random number is?")
    user_guess = int(input())
