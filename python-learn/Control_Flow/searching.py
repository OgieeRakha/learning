shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "hay"
found_at = None

# #for index in range(6):
# for i in range(len(shopping_list)):
#     if shopping_list[i] == item_to_find:
#         found_at = i
#         break

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Item found at {}".format(found_at))

else:
    print("{} not found".format(item_to_find))

