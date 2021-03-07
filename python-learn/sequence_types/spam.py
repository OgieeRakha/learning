#following the PEP 8
menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

word_erase = "spam"
stop = 0
for meal in menu:
    if "spam" not in meal:
        pass
    else:
        for index in range(len(meal) - 1, -1, -1):
            if meal[index] == "spam":
                del meal[index]
            else:
                continue
    print(", ".join(meal))

# for meal in menu:
#     for ingredients in meal:
#         if ingredients.casefold() != "spam":
#             print(ingredients, end=" ")
#     print()


