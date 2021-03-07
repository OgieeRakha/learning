import random
highest = 10
answer = random.randint(1,highest)
print("PLease guess a number between 1 and 10; ")
guess = None

# while guess == None or guess > 0:
while guess != answer:
    guess = int(input("Guess the answer: "))
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

# #another type of conditional statements
# if guess == answer:
#     print("you got it first time")
# else:
#     if guess < answer:
#         print("Please guess higher")
#     else: #guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("well done you guessed it")
#     else:
#         print("sorry, you have not guessed correctly")
