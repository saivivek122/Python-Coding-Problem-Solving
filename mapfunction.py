def squares(x):
    return x * x

numbers = [1,2,3,4,5]
result = map(squares,numbers)
print(list(result))