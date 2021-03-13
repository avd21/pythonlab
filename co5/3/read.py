import csv
file=open('list.csv', 'r') 
read = csv.reader(file)
for row in read:
   print (row)
