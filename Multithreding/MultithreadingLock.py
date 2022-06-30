from threading import *
import threading
import time

def person_1(lock):
    lock.acquire()
    print("Person 1 occupies Meeting Room-1")
    time.sleep(1)
    print("Person 1 vacates the Meeting Room-1")
    lock.release()

def person_2(lock):
    lock.acquire()
    print("Person 2 occupies Meeting Room-1")
    print("Person 2 vacates the Meeting Room-1")
    lock.release()

lock = threading.Lock()

thrd1 = Thread(target=person_1, args=(lock,))
thrd2 = Thread(target=person_2, args=(lock,))

thrd1.start()
thrd2.start()

thrd1.join()
thrd2.join()