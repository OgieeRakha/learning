even = [2,4,6,8]
odd = [1,3,5,7,9]

# even.extend(odd)
new_list = [even, odd]
print(new_list)
for value in new_list:
    print(value)
    for number in value:
        print(number)