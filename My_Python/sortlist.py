i = 0
import collections
import json

lists=[(1015, 'Porky', 'Pig', 3), (1015, 'Wile', 'Coyote', 3), (735, 'Elmer', 'Fudd', 11), (735, 'Road', 'Runner', 11), (1020, 'Goofy', 'Dog', 1), (1001, 'Donald', 'Duck', 2), (831, 'Mickey', 'Mouse', 3), (735, 'Minnie', 'Mouse', 4), (1050, 'Bugs', 'Bunny', 2), (1050, 'Pluto', 'Dog', 2), (1015, 'Wile', 'Coyote', 3), (1015, 'Porky', 'Pig', 3), (805, 'Daisy', 'Duck', 9),
       (735, 'Daffy', 'Duck', 11), (735, 'Road', 'Runner', 11), (735, 'Elmer', 'Fudd', 11)]
# lst = [(5, 7), (2, 3), (0, 3)]
lists.sort(reverse=True,key=lambda x: x[0])
object_list = []
for row in lists:
    d = collections.OrderedDict()
    d['marks'] = row[0]
    d['first_name'] = row[1]
    d['last_name'] = row[2]
    d['Rank'] = row[3]
    object_list.append(d)
j = json.dumps(object_list,default = str)
print(j)