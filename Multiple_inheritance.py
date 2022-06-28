class parent1():
    def __init__(self):
        self.value = 'Inside parent1'

    def show(self):
        print(self.value)

class parent2():
    def __init__(self):
        self.value = 'Inside parent2'
    
    def display(self):
        print("Inside parent2")

class child(parent1,parent2):
    def __init__(self):
        self.value = 'Inside child'
    
    def show(self):
        print(self.value)

obj1 = child()
obj1.show()
obj1.display()