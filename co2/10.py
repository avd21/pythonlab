n=int(input("Enter a Number:"))
factors=[]
print("Factors of",n,"is:")
for i in range(1,n+1):
    if n%i==0:
        print(i)
