value_adm = input("Please enter 3 numbers separated by a comma:")
value_int = value_adm.split(",")

empty_list = []
for i in value_int:
    i = int(i)
    empty_list.append(i)

print(empty_list[0] + empty_list[1] - empty_list[2])
# print(value_int)
# for index in range(len(value_int)):
#     value_int[index] = int(value_int[index])
