available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "hdmi cable"
                   ]
# count = 0
# valid_choices = [str(i) for i in range(1, len(available_parts + 1))]
valid_choices = []
# + 1 is used because of for in range, range doesn't include the last index
for i in range (1, len(available_parts) + 1):
    valid_choices.append(str(i))
current_choice = "-"
computer_parts = [] #creats an empty list

while current_choice != "0":
    if current_choice in valid_choices:
        # the usage of -1 is to make sure that the index that starts from 0, accurately find the parts.
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            print("Removing {}".format(chosen_part))
            computer_parts.remove(chosen_part)
        else:
            print("adding {}".format(chosen_part))
            computer_parts.append(chosen_part)
    else:
        print("Please add options from the list below: ")
        for index, parts in enumerate(available_parts):
            # count += 1
            print("{0}:{1}".format(index + 1, parts))

    current_choice = input("Please pick the parts that you want: ")

print("here is your computer list of computer parts\n{}".format(computer_parts))