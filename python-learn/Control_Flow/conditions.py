age = int(input("kindly fill in your age: "))
if 16 <= age <= 65:
    print("have a good day at work!")
elif age < 16 or age > 65:
    print("kindly get back after you are eligible")
#or we could use elif

print("-" *80)

if age < 16 or age > 65:
    print("kindly get back after you are eligible")
else:
    print("have a good day at work!")