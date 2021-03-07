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
for i in range (1, len(available_parts) + 1):
    valid_choices.append(str(i))
current_choice = "-"
computer_parts = [] #creats an empty list
print(valid_choices)




alphabets = "abcdefghijlkmnopqrstuvwxyz"

for index, character in enumerate(alphabets):
    print(index, character)

print(len(alphabets))

available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "hdmi cable"
                   ]
print(len(available_parts))

