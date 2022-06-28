from tabnanny import check


a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
d = int(input("Enter a number : "))

if d in a+b+c:
    print("yes")