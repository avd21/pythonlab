import csv 
file= open("list.csv", 'w') 
fields = ['SNo', 'Name', 'Roll_No']   
mydict =[{'SNo':'1', 'Name':'arun', 'Roll_No':'101'}, 
         {'SNo':'2', 'Name':'abhi', 'Roll_No':'102'}, 
         {'SNo':'3', 'Name':'raju', 'Roll_No':'103'}] 
writer = csv.DictWriter(file,fields) 
writer.writeheader() 
writer.writerows(mydict) 
file.close()

file= open("list.csv", 'r')
read= csv.DictReader(file)
for row in read:
    print(dict(row))


