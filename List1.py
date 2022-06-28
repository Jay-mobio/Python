a = int(input(""))
b = int(input(""))

list1 = [11, 5, 17, 18, 23, 50]



for i in range(a,b+1):
    if i%2==0:
        print(i)



for i in list1:
    if i%2 == 0:
        list1.remove(i)
print(list1)
