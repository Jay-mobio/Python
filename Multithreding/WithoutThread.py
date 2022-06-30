import time

def square(numbers):
    for n in numbers:
        time.sleep(0.2)
        print("\n Square: ",n*n)

def cube(numbers):
    for n in numbers:
        time.sleep(0.2)
        print("\n Cube: ",n*n*n)
    
arr = [1,2,3,4]

t = time.time()
square(arr)
cube(arr)
print()
print('done in : ',time.time()-t)