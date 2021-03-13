n=int(input("Enter any no.:"))
print("Pyramid of Given no",n,"is")  
for i in range(0, n):
    for j in range(1, i + 2):
        print(j*(i+1), end=' ')
    print("")
  

