def f1(func):
    def f2(*args,**kwargs):
        print("Started")
        val = func(*args,**kwargs)
        print("Ended")
        return val
    return f2

@f1
def add(x,y):
    return x+y
print(add(5,5))