from concurrent.futures import thread
from threading import *
def test():
    print('Child thread \n')

t = Thread(target=test)
t.start()

print('Main thread identification number is :',current_thread().ident)
print('Child thread identification number is :',t.ident)
