class parent():
    def __init__(self):
        self.value = 'Inside parent'

    def show(self):
        print(self.value)

class child(parent):
    def __init__(self):
        self.value = 'Inside child'
    
    def display(self):
        print("Inside parent")

class grandchild(child):
    def __init__(self):
        self.value = 'Inside grandchild'
    
    def show(self):
        print(self.value)

g = grandchild()
g.display()
g.show()