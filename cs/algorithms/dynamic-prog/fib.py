import time

# import time for recording function call durations

# The maximum n can be for my computer to take atleast 5 seconds is about 30-40
def fib_recursive(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_recursive(n - 1) + fib_recursive(n - 2)

    return result


# n can be 200 and my computer will compute this instantly,
# since memoization stores the results
def fib_memo(n, memo):
    if memo[n] is not None:
        return memo[n]
    elif n == 1 or n == 2:
        result = 1
    else:
        result = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)

    memo[n] = result
    return result


# this approach will define an array up to n+1,
# containing the fibonacci sequence.
# Lastly, we just access the nth element of this array, which is much faster than recursion, about the same as memoization
def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1

    # Initialise array with size n + 1
    bottom_up = [None for i in range(n + 1)]
    # indexes 1 and 2 should be 1
    bottom_up[1] = 1
    bottom_up[2] = 1

    # iteratively define the fibonacci sequence in the array
    for i in range(3, n):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]

    # access n-th index
    return bottom_up[n]


def record_function_call(func, n, type):
    before = 0
    after = 0

    if type != "recursive" and type != "memoization" and type != "bottom-up":
        return None

    if type == "recursive" or type == "bottom-up":
        before = time.time() * 1000
        func(n)
        after = time.time() * 1000.0

    elif type == "memoization":
        before = time.time() * 1000
        func(n, [None for i in range(n + 1)])
        after = time.time() * 1000.0

    print(
        "\n"
        + type.upper()
        + "\n\tn = "
        + (str)(n)
        + ", t = "
        + (str)(round(after - before, 10))
        + "\n"
    )


_input = ""
_n = 35

while _input != "x":
    _input = input(
        "\n1) Change n\n2) Perform recursion\n3) Perform memoization\n4) Perform bottom-up\n0) Exit\n\n>"
    )

    if _input == "0":
        break
    elif _input == "1":
        _n = int(input("Choose a new value for n:\n>"))
        continue
    elif _input == "2":
        record_function_call(fib_recursive, _n, type="recursive")
        continue
    elif _input == "3":
        record_function_call(fib_memo, _n, type="memoization")
        continue
    elif _input == "4":
        record_function_call(fib_bottom_up, _n, type="recursive")
        continue
