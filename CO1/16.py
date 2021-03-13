print("The given strings are:")
a="Hello"
b="World"
print(a,b)
x=a[0:1]
a=a.replace(a[0:1],b[0:1])
b=b.replace(b[0:1],x)
print("After the swaping the 1st character of strings are:")
print(a,b)

