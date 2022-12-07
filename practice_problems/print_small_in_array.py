arr = [23,1,23,45,67,0]
def print_least(arr):
    least = arr[0]
    for i in range(0,len(arr)):
        if arr[i] < least:
            least = arr[i]
    return least
print(print_least(arr))