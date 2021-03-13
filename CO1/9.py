w = input("Enter your word : ")
temp1 = w[0]
temp2 = w[-1]
l = len(w)
result = w[-1]+w[1:l-1]+w[0]
print("Exchanged the first and last characters:",result)
