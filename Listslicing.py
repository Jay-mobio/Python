List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
 
List[:6] = []
newList = List[:3]+List[7:]
print(List[-1:-1:-1])
print(List[10::2])
print(List[:1:-2])
print(List[::-3])
print(List[::-1])
print(List[::])
print(List[3:9:2])
print(List[::2])
print(newList)
List1 = List[::2]+List[1::2]
print(List1)