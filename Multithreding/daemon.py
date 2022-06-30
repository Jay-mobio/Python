import threading
def job1():
    print("Executed by t1")

t1 = threading.Thread(target=job1)
print(t1.isDaemon())
t1.setDaemon(True)
print(t1.isDaemon())
