a = [1,2,3,4,5,6,7,8,9]
b = []

for x in range (10,20):
    if x % 2 == 0:
        b.append(x)
print('appended even numbers from 10 to 20 ', b)

b.extend(a)
print('List exyended',b)

b.clear()
print('list cleared:',b)
b = a.copy()
print('list copied from a ', b)
c = a.count(2)
print('counted element 2 :',c)
d = b.pop(4)
print('poped at index 4 :',b)
print('poped number :',d)
a.reverse()
print('list reversed :',a)
a.sort()
print('list sorted',a)
a.remove(4)
print('removed element 4',a)