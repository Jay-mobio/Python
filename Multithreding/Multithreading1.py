import time
import threading

def square(numbers):
    for n in numbers:
        time.sleep(0.2)
        print("Square: ",n*n)

def cube(numbers):
    for n in numbers:
        time.sleep(0.2)
        print("Cube: ",n*n*n)
    
arr = [1,2,3,4]

t = time.time()
t1 = threading.Thread(target=square, args=(arr,))
t2 = threading.Thread(target=cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()



print('done in : ',time.time()-t)