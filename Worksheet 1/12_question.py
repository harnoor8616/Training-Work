# Create list1 = [1, 2, 3], list2 = list1, list3 = [1, 2, 3]. Compare their IDs.
list1 = [1, 2, 3]
list2 = list1   
list3 = [1, 2, 3]
print("ID of list1:", id(list1))
print("ID of list2:", id(list2))
print("ID of list3:", id(list3))
print("Are the IDs of list1 and list2 the same?", id(list1) == id(list2))
print("Are the IDs of list1 and list3 the same?", id(list1) == id(list3))
print("Are the IDs of list2 and list3 the same?", id(list2) == id(list3))
print("Are the IDs of list1, list2, and list3 all the same?", id(list1) == id(list2) == id(list3))