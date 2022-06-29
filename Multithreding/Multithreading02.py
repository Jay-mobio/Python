from concurrent.futures import thread
from threading import *
def display():
    for i in range(2):
        print("Child hread")


t = Thread(target=display)
t.start()
t.join()

for i in range(2):
    print("main thread")
current_thread().name='jay'
print(current_thread().getName())
