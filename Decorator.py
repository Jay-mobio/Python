def decorator(func):
    def wrapper():
        print("This is printed before function")
        func()
        print("This is printed after function")
    return wrapper

def say_hello():
    print("The function is executing")

say_hello = decorator(say_hello)
say_hello()