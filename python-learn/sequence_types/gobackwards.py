data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]
min_valid = 100
max_valid = 200

#we need to determine which index in data to delete,
#hence, even though reversed, we are still deleting in a
#forward manner

top_index = len(data) - 1
for index, value in enumerate(data):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]

print(data)



# for i in range(len(data) - 1, -1, -1):
#     if data[i] < min_valid or data[i] > max_valid:
#         print(data[i])
#         del data[i]
#     else:
#         continue

