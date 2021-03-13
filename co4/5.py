class publisher:
    def __init__(self,pubname):
        self.pubname=pubname
  
class book(publisher):
    def __init__(self,pubname,title,author):
        publisher.__init__(self,pubname)
        self.title=title
        self.author=author

class python(book):
    def __init__(self,pubname,title,author,price,no_of_pages):
        book.__init__(self,pubname,title,author)
        self.price=price
        self.no_of_pages=no_of_pages
    def display(self):
        print("Publisher:",self.pubname)
        print("Title:",self.title)
        print("Author:",self.author)
        print("Price:",self.price)
        print("No of pages:",self.no_of_pages)
b1=python("Rupa Publications","The 3 Mistakes Of My Life","Chetan Bhagat",140,260)
b1.display()

