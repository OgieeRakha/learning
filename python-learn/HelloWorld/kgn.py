#          012345678901234567890123456
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]
print(backwards)

bwd = letters[25::-1]
print(bwd)

print(letters[::-1])

ans_backwards = "zyxwvutsrqponmlkjihgfedcb"
ans_bwd = "zyxwvutsrqponmlkjihgfedcba"

#challenge
print()
print(letters[16:-13:-1])
print(letters[4::-1])
print(letters[:-9:-1])
#qpo
#edcba
#zyxwvuts

print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])

#wxyz
#z
#a works on an empty string
#a