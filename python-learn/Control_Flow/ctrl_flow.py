name = input("What is your name? ")
age = int(input("What is your age, {0}? ".format(name)))

if age < 18:
    print("Please comeback in {0} years".format(18 - age))

elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")
else:
    print("You're old enough to vote")
    print("Please put an X in the box")