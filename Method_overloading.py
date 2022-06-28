class methodoverloading:
    def hello(self,name = None):
        if name is not None:
            print('Hello '+name)
        else:
            print('Hello')

obj = methodoverloading()
obj.hello()
obj.hello('Jay')