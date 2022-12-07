arr = [1,2,3,4,5,6,7,8,9]
def print_odd(arr):
    data = []
    for i in range(0,len(arr),2):
        data.append(arr[i])
    return  data
print(print_odd(arr))