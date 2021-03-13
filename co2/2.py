n=int(input("Enter the number of terms : "))
a=0
b=1
print("Fibonacci series of",n,"terms:")
print(a)
print(b)
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c)

