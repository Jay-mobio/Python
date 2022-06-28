from abc import abstractclassmethod,ABC

class CAR(ABC):
    def mileage(self):
        pass

class Tesla(CAR):
    def mileage(self):
        print("Mileage is 30kmpl")

class duster(CAR):
    def mileage(self):
        print("Mileage is 25kmpl")

class suzuki(CAR):
    def mileage(self):
     print("Mileage is 22kmpl")

t = Tesla()

t.mileage() 

d = duster()
d.mileage()

s = suzuki()
s.mileage()