class Time:
    def __init__(self,h,m,s):
        self.hour=h
        self.minute=m
        self.second=s

    def time(self):
        if self.second>=60:
            self.second-=60
            self.minute+=1
        if self.minute>=60:
            self.minute-=60
            self.hour+=1
        return("%.2d:%.2d:%.2d"%(self.hour,self.minute,self.second))
    def _add_(self,other):
        _hour=self._hour+other.hour
        _minute=self._minute+other.minute
        _second=self._second+other.second
        return("%.2d:%.2d:%.2d"%(hour,minute,second))

t1=Time(2,60,60)
print("TIME 1",t1.time())
t2=Time(4,50,5)
print("TIME 2",t2.time())
print("Sum")
print(t1 + t2)

