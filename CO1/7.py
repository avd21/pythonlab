list1 = [10,8,5,12,6,9,3]
list2 = [13,4,9,2,5]
print("List1:",list1)
print("List2:",list2)
if(len(list1)==len(list2)):
    print("Lists are of same length")
else:
    print("Lists are not of same length")
if(sum(list1)==sum(list2)):
    print("Lists are of same sum")
else:
    print("Lists are not of same sum")

print("Values occur in both:")
for x in list1:
    for y in list2:
        if x == y:
          print(y)
         
