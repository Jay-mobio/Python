list1 = ["apple","banana","kiwi","mango","grapes"]
list2 = []
for i in list1:
    if "a" in i:
        list2.append(i)
print(list1)
print(list2)

list3=[x for x in list1 if x !="apple"]
print(list3)

list4 = [x for x in range(10) if x < 5]
print(list4)

list5 = [x.upper() for x in list1]
print(list5)

list6 = ['AAA' for x in list1]
print(list6)


list7 = [x if x != "banana" else "orange" for x in list1]
print(list7)