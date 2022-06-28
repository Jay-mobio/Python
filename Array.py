import array as arr
a = arr.array('i',[2, 5, 62, 5, 42, 52, 48, 5])
print(a[2:5])

odd = arr.array('i',[1,3,5])
even = arr.array('i',[2,4,6])

numbers = odd + even
print(numbers)

a.insert(2,55)
a.extend([7,7,7])
print(a)
print(a.index(62))
print(a.count(2))
print(a.sort())