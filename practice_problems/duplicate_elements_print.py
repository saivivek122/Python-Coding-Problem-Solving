arr = [2,2,2,3,3,3,5]
arr2 = []
# my_dict = {1: 'apple', 2: 'ball'}
repeated = {}
for ele in arr:
    repeated[ele] = arr.count(ele)
    # try:
    #     repeated[ele] +=1
    # except:
    #     repeated[ele] = 1
print(repeated)
for item in repeated:
    if repeated[item] > 1:
        arr2.append(item)
print(arr2)
# for item in my_dict:
#     print(item)
# print(my_dict[1])
print(arr[::-1])
arr.reverse()
print(arr)