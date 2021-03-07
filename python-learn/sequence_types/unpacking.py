#we could easily assign a value into a variable
#and this happens to be the easiest way to do one
a = b = c = d = e = f = 42
print(c)

x, y, z = 1, 2, 76
print(x)
print(y)
print(z)

data = 1, 2, 76
x, y, z = data
print(x)
print(y)
print(z)

#trying to unpack a list
data_list = 1, 2, 76
x, y, z = data_list
print(data_list)
