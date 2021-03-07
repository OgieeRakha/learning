# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191, 350, 360]
# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191, 350, 360]
# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191]
# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191]
data = []
data.sort()

stop = 0
for index, value in enumerate(data):
    if value >= 100 :
        stop = index
        break
print(stop)
del data[:stop]
print(data)

print(len(data))

start = 0
for index in range(len(data) - 1, -1, -1):
    if data[index] <= 200:
        #we have the index of the alst item to keep.
        #set "start" to the position of the first
        #item to delete, which is 1 after 'index'
        start = index + 1
        break
del data[start:]
print(data)



# for index, value in enumerate(data):
#     if value > 200:
#         stop = index
#         break
# del data[stop:]
# print(data)