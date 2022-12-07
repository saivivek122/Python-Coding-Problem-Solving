def factorial(n):
    assert 0 <= n == int(n), "The num should be positive integer only"
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(1.5))
