arr = [1, 5,9]
max_till_now = 0
max_ending = 0
k = max(arr)
count = []
if k < 0:
    print(k)
else:
    for i in range(0,len(arr)):
        max_ending = max_ending + arr[i]
        if max_ending < 0:
            max_ending = 0
        elif max_till_now < max_ending:
            max_till_now = max_ending
            count.append(max_till_now % 5)

    print(max_till_now)
    print(count)
    print(max(count))
