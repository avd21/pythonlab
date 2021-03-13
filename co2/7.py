l=input("Enter a word:")
last=l[-3:]
if(last=="ing"):
    l=l+"ly"
else:
    l=l+"ing "
print(l)
