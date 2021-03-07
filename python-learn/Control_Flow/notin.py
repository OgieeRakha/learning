# activity = input("What would you like to do today? ")
# if "cinema" not in activity.casefold():
#     print("But I want to go to the cinema")

#The If Challenge

name = input("What is your name? ")
age = int(input("How old are you? "))

if 18 <= age < 31:
    print("Welcome to the holiday {} you're eligible because you're already {} years old"
          .format(name,age))
else:
    print("I'm sorry {} but you could enjoy other holidays".format(name))
