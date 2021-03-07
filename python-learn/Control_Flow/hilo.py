low = 1
high = 1000

print("Please think of a number between {} and {}"
      .format(low,high))
input("Press Enter to start")

guesses = 1
while high != low:
    print("guessing in the range from {} to {}".format(low,high))
    guess = low + (high - low) // 2
    guesses += 1
    high_low = input("My guess is {}. Should i guess "
                     "higher or lower? Enter h or l or c "
                     "if my guess was correct.".format(guess)).casefold()
    if high_low == "h":
        #Guess higher. The low end of the range becomes 1 greater than the guess
        low = guess + 1
    elif high_low == "l":
        #Guess lower. the high end of the range becomes 1 less than the guess
        high = guess - 1
    elif high_low == "c":
        print("Your answer is {0}, i got it in {1} guesses"
              .format(high_low, guesses))

else:
    print("huh i know what you're thinking, you're thinking {}".format(high))
    print("and i guessed it in {} guesses".format(guesses))