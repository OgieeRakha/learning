def multiply(x: float, y: float) -> float:
    """
    Creates a multiplication value between two arguments.

    :param x: the first argument that is inputted, must be an `int`.

    :param y: the second argument that is inputted, must be an `int`.

    :return: returns the value of multiplication between the two argumeents.
    """
    result = x * y
    return result


def fibonacci(n: int) -> int:
    """Return the `n` th Fibonacci number, for positive `n`"""
    if 0 <= n <= 1:
        return n
    n_minus1, n_minus2 = 1, 0

    result = None

    for f in range(n-1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range (36):
    print(i, fibonacci(i))



answer = multiply(10.5, 4)
print(answer)

forty_two = multiply(6, 7)
print(forty_two)

print()
for val in range(1,5):
    two_times = multiply(2, val)
    print(two_times)



