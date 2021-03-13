w = input("Enter your word : ")
char = w[0]
w = w.replace(char,"$")
w = char+w[1:]
print("First character replaced with ‘$’ except first character:",w)

