from multiprocessing import Process, Pipe
def myfunction(conn):
   conn.send(['hi!! I am Python'])
   conn.close()
if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=myfunction, args=(child_conn,))     
    p.start()
    p.join()
    print (parent_conn.recv())