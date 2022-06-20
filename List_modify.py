mylist = ["apple", "banana", "cherry"]
mylist2 = ["mango", "pineapple", "papaya"]
thistuple = ("kiwi", "orange")

print(mylist) 
print(mylist)
print(len(mylist))
print(mylist[1])
print(mylist[-1])
print(mylist[2:5])
print(mylist[:4])
print(mylist[-4:-1])
if "apple" in mylist:
  print("Yes, 'apple' is in the fruits list")
mylist[1] = "blackcurrant"
print(mylist)
mylist.insert(2, "watermelon")
print(mylist)
mylist.append("orange")
print(mylist)
mylist.extend(mylist2)
print(mylist)

mylist.extend(thistuple)
mylist.pop(1)
print(mylist)

  
