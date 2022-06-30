from threading import Thread, current_thread
from queue import Queue
import time

def worker(q):
    while True:
        value = q.get()
        print(f'\n in {current_thread().name} got {value}')
        q.task_done()

if __name__ == "__main__":
    q = Queue()
    num_thread = 10
    for i in range (num_thread):
        thread = Thread(target=worker,args=(q,))
        thread.daemon = True
        thread.start()

    for i in range(1,21):
        q.put(i)
    q.join()