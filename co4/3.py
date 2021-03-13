class rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        a=self.length*self.breadth
        return a
a=int(input("Enter the length of the reactangle 1:"))
b=int(input("Enter the breadth of the reactangle 1:"))
c=int(input("Enter the length of the reactangle 2:"))
d=int(input("Enter the breadth of the reactangle 2:"))
obj1=rectangle(a,b)
obj2=rectangle(c,d)
print("Area of rectangle 1:",obj1.area())
print("Area of rectangle 2:",obj2.area())

if obj1.area() > obj2.area():
     print("Rectangle 1: is greater ",obj1.area())
else:
    print("Rectangle 2: is greater ",obj2.area())

