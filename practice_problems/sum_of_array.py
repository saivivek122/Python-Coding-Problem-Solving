arr = [1,2,3,4,5]
def cal_sum(arr):
    sum = 0
    for i in range(0,len(arr)):
        sum+=arr[i]
    return sum
print(cal_sum(arr))