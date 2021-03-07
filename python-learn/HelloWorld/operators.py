a = 12
b = 3
print (a + b)   #15
print (a - b)   #9
print (a * b)   #36
print (a / b)   #4.0 division will always produce float result
print (a // b)  #4 integer division, rounded down towards minus infinity
print (a % b)   #0 modulo: the remainder after integer division

print()

for i in range( 1 ,a // b): #if we would place it with normal division, float will create syntax error
    print(i)

a = 12
b = 3
print (a + b)
print (a - b)
print (a * b)
print (a / b)
print (a // b)
print (a % b)

for i in range( 1 ,a // b):
    print(i)

print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))
print((((a+b) / 3) - 4) * 12)
print(((a + b) / 3 - 4)* 12)

c = a+b
d = c/3
e = d-4
print(e*12)