f1=open("file.txt","r")
f2=open("file2.txt", "w") 
l=f1.readlines()
 
for i in range(0,len(l)) :
  if(i%2==0):
    f2.write(l[i]) 
    f1.close()
f2.close()

f1=open("file.txt","r")
f2=open("file2.txt", "r")  
l1=f1.read()
l2=f2.read()
print("Contents of File 1:")
print(l1)
print("Copy odd lines of File 1 to File 2:")
print(l2)
f1.close()
f2.close()


   
