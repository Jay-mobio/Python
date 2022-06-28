class students():
    def setName(self,n):
        self.__name = n
    
    def getName(self):
        return self.__name
    
    def setMarks(self,m):
        self.__marks = m
    
    def getMarks(self):
        return self.__marks

    def display(self):
        print('Name : ',self.__name)
        print('Marks : ',self.__marks)

s = students()
s.setName('Jay')
s.getMarks(70)
s.display()