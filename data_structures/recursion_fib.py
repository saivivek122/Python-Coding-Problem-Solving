import sys
sys.setrecursionlimit(10000)
# def fibonacci(n):
#     assert 0 <= n == int(n), "Fib should be positive integers"
#     if n in [0, 1]:
#         return n
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# print(fibonacci(12))


# Function for nth fibonacci number - Dynamic Programming
# Taking 1st two fibonacci nubers as 0 and 1

FibArray = [0, 1]


def fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n <= len(FibArray):
        return FibArray[n - 1]
    else:
        temp_fib = fibonacci(n - 1) + fibonacci(n - 2)
        FibArray.append(temp_fib)
        return temp_fib


# Driver Program

print(fibonacci(124))
