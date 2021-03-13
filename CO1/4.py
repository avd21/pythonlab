a="hello world hello friends"
print(a)
s=a.split(' ')
count = {}
print
for n in s:
   count[n]=count.get(n,0)+1   
print("The occurrences of each word in a given line is :")
print(count) 
