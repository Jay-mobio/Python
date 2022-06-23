import multiprocessing
def cube(num):
    print("Cube {}".format(num*num*num))

def square(num):
    print("Square {}".format(num*num))

if __name__ == "__main__":

    p1 = multiprocessing.Process(target=square, args=(10, ))
    p2 = multiprocessing.Process(target=cube, args=(10, ))

    p1.start()
    p2.start()

    p1.join()
    p2.join()