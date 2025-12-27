# Magic methods = Dunder methods __init__ , __str__ , __eq__  
#                 They are automatically called by many of Python's built-in operations.
#                 They allow developers to define or customize the behavior of objects

class Book:

    def __init__(self,title,author,num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    # generally dunder str used to customize output displayed when we print an object directly .
    def __str__(self):
        return f"{self.title} written by {self.author} of {self.num_pages} pages"
    # generally dunder eq used to compare two objects are equal or not by returning some boolean value .
    def __eq__(self,other):
        return self.title == other.title and self.author == other.author
    def __lt__(self,other):
        return self.num_pages < other.num_pages
    def __gt__(self,other):
        return self.num_pages > other.num_pages
    def __add__(self,other):
        return f"{self.num_pages+other.num_pages} pages"
    def __contains__(self,givenval):
        return givenval in self.title or givenval in self.author
    def __getitem__(self,keyval):
        if keyval == "title":
            return self.title
        if keyval == "author":
            return self.author
        if keyval == "num_pages":
            return self.num_pages
        else:
            return f"the given key {keyval} is not avalable ."

book1 = Book("let us c","Yeshwanth Kanethkar",950)
book2 = Book("inorganic chemistry","jd lee",1900)
book3 = Book("single life","myself",0)
book4 = Book("single life","myself",0)

print(book1)
print(book2)
print(book3)

print(book1 == book2)
print(book3 == book4)

print(book1 < book2)
print(book1 > book2)
print(book1+book2)
print("inorganic" in book2)
print(book1["title"])
print(book1["author"])
print(book1["num_pages"])
print(book1["audio"])

