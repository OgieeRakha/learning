answer = None
a1 = "Learn Python"
a2 = "Learn Java"
a3 = "Go Swimming"
a4 = "Have Dinner"
a5 = "Go to bed"
a6 = "Exit"

while answer != 0:
    print("Please choose your option from the list below: \n1. {}\n2. {}\n3. {}"
      "\n4. {}\n5. {}\n6. {}\n".format(a1,a2,a3,a4,a5,a6))
    answer = int(input("Please select the activity through its number: "))
    if answer == 1:
        print("Go ahead and  {}".format(a1))
    elif answer == 2:
        print("Go ahead and  {}".format(a2))
    elif answer == 3:
        print("Go ahead and  {}".format(a3))
    elif answer == 4:
        print("Go ahead and  {}".format(a4))
    elif answer == 5:
        print("Go ahead and  {}".format(a5))
    elif answer == 0:
        print("Okay do your thing!")
        print("Thank you for participating")
        break
    else:
        print("kindly put a valid number")
        continue
