i = 0
j = 0
k = []
count = 0
list3 = []
check_list = []
from collections import Counter

lists = [(1015, 'Porky', 'Pig', 3), (1015, 'Wile', 'Coyote', 3), (735, 'Elmer', 'Fudd', 11),
         (735, 'Road', 'Runner', 11), (1020, 'Goofy', 'Dog', 1), (1001, 'Donald', 'Duck', 2),
         (831, 'Mickey', 'Mouse', 3), (735, 'Minnie', 'Mouse', 4), (1050, 'Bugs', 'Bunny', 2),
         (1050, 'Pluto', 'Dog', 2), (1015, 'Wile', 'Coyote', 3), (1015, 'Porky', 'Pig', 3),
         (805, 'Daisy', 'Duck', 9),
         (735, 'Daffy', 'Duck', 11), (735, 'Road', 'Runner', 11), (735, 'Elmer', 'Fudd', 11)]

while i < len(lists):
    k.append(lists[i][0])
    i = i + 1
repeated = {}
for i in k:
    repeated[i] = k.count(i)
print(repeated)
data = list(repeated.items())
data2 = []
for row in data:
    data2.append(row)
print(data2)

list_of_tuples = [(1, 2), (4, 5)]
list_of_lists = [list(elem) for elem in list_of_tuples]
print(list_of_lists)