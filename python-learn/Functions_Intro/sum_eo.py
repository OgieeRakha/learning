# first we need to define a function
def sum_eo(highest, even_odd):
    """
    A function that sums the odd or even numbers.

    Returns a value of the sum.

    :param highest: The highest number that would indicate the maximum value through
        a certain range `int`.
    :param even_odd: The first character between even and odd to indicate what
        type of calculation will be done.
    :return: returns a value of sum 1st argument range based on
        even or odd numbers.
    """
    total_sum = 0
    if even_odd.casefold() == "o":
        for val in range(highest):
            if val % 2 != 0:
                total_sum += val
        return total_sum
    elif even_odd.casefold() == "e":
        for val in range(highest):
            if val % 2 == 0:
                total_sum += val
        return total_sum
    else:
        return -1


def get_integer(prompt):
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)
        # else:
        print("This is an invalid number")


def convert(lists):
    return tuple(lists)


def creating_tuples(lists, integers, strings):
    lists.append(integers)
    lists.append(strings)
    return convert(lists)


while True:
    # prompting for input from the user
    answer_int = get_integer("Please input a number: ")
    answer_str = input("Please input e/o: ")
    if answer_str.casefold() != "end":
        print((sum_eo(answer_int, answer_str)))
    else:
        print("Thank you for using the program!")
        break



# # creating tuples from the answers
# sum_answer = creating_tuples(empty_list, answer_int, answer_str)
# # unpacking a tuple
# calculation = sum_eo(x, y)
# print(calculation)