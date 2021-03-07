number = 5
multiplier = 8
answer = 0
mult = 0

# add your loop after this comment
while mult != multiplier:
    answer += number
    mult += 1

print(answer)

# or we could use it with for
for i in range(multiplier):
    answer += number
print(answer)