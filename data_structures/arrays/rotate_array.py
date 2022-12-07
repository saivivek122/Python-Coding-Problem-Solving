test = '1'
test = int(test)
size_test = '5 2'
size_test = size_test.split()
array = '1 2 3 4 5'
out_put = ""
array = array.split()
for i in range(int(size_test[1])):

    array = array[-1:] + array[:int(size_test[0])-1]

for i in array:
    out_put = out_put + " " + i
print(out_put)



