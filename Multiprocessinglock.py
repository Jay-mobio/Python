from multiprocessing import Process
import multiprocessing
import time

def deposit(balance):
    for i in range(100):
        lock.acquire()
        time.sleep(0.01)
        balance.value = balance.value + 1
        lock.release()

def withdraw(balance):
    for i in range(100):
        lock.acquire()
        time.sleep(0.01)
        balance.value = balance.value - 1
        lock.release()

if __name__ == "__main__":
    balance = multiprocessing.Value('i',200)
    lock = multiprocessing.Lock
    d = Process(target=deposit, args=(balance,))
    w = Process(target=withdraw, args=(balance,))
    
    d.start()
    w.start()
    
    d.join()
    w.join()
    
    print(balance.value)