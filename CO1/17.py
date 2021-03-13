l={"Vicky":30,"Sachin":10,"Arun":50,"Pinky":20,"Rahul":40}
print (l)
a=sorted(l.items())
print('Ascending Order:',a)
d=sorted(l.items(),reverse=True)
print('Descending Order:',d)
print("Sorting by values:")
s=sorted(l.values())
print(s)

