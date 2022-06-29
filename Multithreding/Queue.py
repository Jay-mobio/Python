import queue
from threading import *
q = queue.Queue()

for val in range(5):
    q.put(val)

while not q.empty():
    print(q.get())

q.qsize()



def get_in_thread():
    print("Thread started")
    print("The thread gets the value = ",q.get())

th = Thread(target=get_in_thread)
th.start()

def add_in_queue():
    try:
        q.put(200, block = False)
    except queue.Full:
        print("Queue is full")

add_in_queue()

def get_in_queue_timeout():
    try:
        q.get(block = True,timeout=2)
    except queue.Empty:
        print("Queue is empty")

while not q.empty():
    print(q.get())
    