import _thread
import os
import threading

def task1():
    print("Task 1 is assigned to thread {}.".format(threading.current_thread().name))
    print("ID of processing running task {}.".format(threading.current_thread().name))

def task2():
    print("Task 2 is assigned to thread {}.".format(threading.current_thread().name))
    print("ID of processing running task {}.".format(threading.current_thread().name))

if __name__ == "__main__":
    print("ID of processing running main program : {}.".format(os.getpid()))
    print("Main thread name : {}.".format(threading.current_thread().name))

    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task1, name='t2')

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
