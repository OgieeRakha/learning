def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()

test = (input("Enter a word to be checked: "))
if is_palindrome(test):
    print("'{}' is actually a palindrome".format(test))
else:
    print("'{}' is not a palindrome".format(test))

