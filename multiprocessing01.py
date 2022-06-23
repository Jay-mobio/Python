import multiprocessing
import os

def work1():
    print("ID of the process running work1 : {}".format(os.getpid()))

def work2():
    print("ID of the process running work2 : {}".format(os.getpid()))

if __name__=="__main__":
    print("ID of the main process : {}".format(os.getpid()))

    p1 = multiprocessing.Process(target=work1)
    p2 = multiprocessing.Process(target=work2)

    p1.start()
    p2.start()

    print("ID of proces p1: {}".format(p1.pid))
    print("ID of process p2: {}".format(p2.pid))

    p1.join()
    p2.join()

    print("Both processes is finished execution")

    print("Process p1 is alive: {}".format(p1.is_alive()))
    print("Process p2 is alive: {}".format(p2.is_alive()))