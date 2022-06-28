class cat:
    def __init__(self,name,age):
        self.age = age
        self.name = name
    
    def info(self):
        print("Hi  i am a cat. My namem is {0}. and my age is {1}".format(self.name,self.age))
    
    def make_sound(slef):
        print("Meow")

class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def info(self):
        print("Hi i am a dog. My name is {0} and my age is {1}".format(self.name,self.age))
    
    def make_sound(self):
        print("Bark")
    
cat1 = cat('Kitty',2)
dog1 = dog("fluffy",5)
cat1.info()
cat1.make_sound()
dog1.info()
dog1.make_sound()