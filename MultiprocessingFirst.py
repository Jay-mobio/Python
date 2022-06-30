from multiprocessing import Process
def cube(my_numbers):
   for x in my_numbers:
      print('%s cube is %s' % (x, x**3))

def square(my_numbers):
   for x in my_numbers:
      print('%s square is %s' % (x, x**2))
      
if __name__ == '__main__':
   my_numbers = [1,2,3,4]
   p1 = Process(target=cube, args=(my_numbers,))
   p2 = Process(target=square, args=(my_numbers,))
   p1.start()
   p2.start()
   p1.join
   p2.join
   print ("Done")