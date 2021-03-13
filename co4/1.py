class rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        a=self.length*self.breadth
        return a
    def perimeter(self):
        b=2*(self.length+self.breadth)
        return b

    
a=int(input("Enter the length of the reactangle 1:"))
b=int(input("Enter the breadth of the reactangle 1:"))
c=int(input("Enter the length of the reactangle 2:"))
d=int(input("Enter the breadth of the reactangle 2:"))
obj1=rectangle(a,b)
obj2=rectangle(c,d)
print("Area of rectangle 1:",obj1.area(),"And","Premeter of rectangle 1:",obj1.perimeter())
print("Area of rectangle 2:",obj2.area(),"And","Premeter of rectangle 2:",obj2.perimeter())

if obj1.area() == obj2.area():
     print("Area of Both rectangle is same")
else:
    print("Area of Both rectangle is not Same")

