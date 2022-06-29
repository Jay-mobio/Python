from threading import *
def job1():
    print("Executed by t1")
    t2 = Thread(target=job2)
    print("T2is daemon: ",t2.isDaemon())
    t2.start()

def job2():
    print("Executed by t2")

t1 = Thread(target=job1)
t1.setDaemon=(True)
print("T1 is daemon :",t1.isDaemon)
t1.start()
