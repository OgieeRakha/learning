#break challenge:
# Modify the code inside this loop to stop when i is greater than zero and exactly divisible by 11
for i in range(1,20):
    if i % 3 > 0 and i % 5 > 0:
        print (i)

for i in range(1,20):
    if i % 3 == 0 or i % 5 == 0:
        continue
    else:
        print(i)



#
# for i in range(0, 100, 7):
#     print(i)
#     num = i/7
#     if num % 11 == 0 and num > 0:
#         break

