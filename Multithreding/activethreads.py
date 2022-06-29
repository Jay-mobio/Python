from threading import *
import time

def display():
    print(current_thread().name,'...started ')
    time.sleep(3)
    print(current_thread().name,'...ended ')
    

print("The number ofactive threads are :", active_count())

t1 = Thread(target=display,name='ChildThread-1')
t2 = Thread(target=display,name='ChildThread-2')
t3 = Thread(target=display,name='ChildThread-3')

t1.start()
t2.start()
t3.start()
print()
print(t1.name,'Is Alive',t1.is_alive())
print(t2.name,'Is Alive',t2.is_alive())
print(t3.name,'Is Alive',t3.is_alive())

l = enumerate()

for t in l:
    print("Thread name : ",t.name)
    print("Thread identification number ", t.ident)
    print()

print("Number of active threads :",active_count())
time.sleep(10)
print(t1.name,'Is Alive',t1.is_alive())
print(t2.name,'Is Alive',t2.is_alive())
print(t3.name,'Is Alive',t3.is_alive())
print("Number of active threads :",active_count())

