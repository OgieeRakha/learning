import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting the user, until valid
    `int` is entered
    :param prompt: The String that the user will see when they're prompted
    to enter the value
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print("This is an invalid number")


highest = 1000
answer = random.randint(1,highest)
print("PLease guess a number between 1 and 10; ")
guess = 0

# while guess == None or guess > 0:
while guess != answer:
    guess = get_integer(": ")
    if guess == answer:
        print("Congratulations, you guessed the right answer")
    elif guess == 0:
        print("Why you give up? you loser.")
        break
    else:
        if guess > answer:
            print("guess lower")
        else:
            print("guess higher")
        continue
