def palindrome_sentence(string):
    """
     Create a list that would be joined to create a `string`.

    The function will separate all other characters that aren't a alphanumeric value.

    :param string: The strings that would be checked.
    :return: The alphanumerical strings without any other connecting characters.
    """
    new_list = []
    for word in string:
        if word.isalnum() is True:
            new_list.append(word)
        else:
            continue
    new_string = "".join(new_list)
    return is_palindrome(string)


def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()


while True:
    word_check = input("Kindly fill in a sentence to check"
                   "if it's a palindrome or not?\n")
    if word_check != "0":
        if palindrome_sentence(word_check):
            print("The '{}' is in fact a palindrome"
              .format(word_check))
        else:
            print("The '{}' is not a palindrome".format(word_check))
    else:
        print("Thank you for checking your words"
              " with us.")
        break