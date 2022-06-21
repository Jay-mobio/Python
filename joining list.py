list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = [4,5,6]
list4 = [7,8,9]
list5 = [10,11,12]
list6 = [13,14,15]

list = list1 + list2
print(list)

for x in  list3:
    list4.append(x)
print(list4)

list6.extend(list5)
print(list6)

