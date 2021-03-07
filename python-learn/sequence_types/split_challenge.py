generated_list = ["9", " ",
                  "2", "2", "3", " ",
                  "3", "7", "2", " ",
                  "0", "3", "6", " ",
                  "8", "5", "4", " ",
                  "7", "7", "5", " ",
                  "8", "0", "7",
                  ]
values = "".join(generated_list)
values_list = values.split()
print(values_list)

new_list = []

for index in range(len(values_list)):
    values_list[index] = int(values_list[index])
print(type(values_list))
print(sum(values_list))

# integer_values = []
# for value in values_list:
#     integer_values.append(int(value))
# print(integer_values)
# print(sum(integer_values))

# for num in values:
#     if num in "1234567890":
#         num = int(num)
#         new_list.append(num)
#     else: continue
#
# print(new_list)
# print(sum(new_list))
