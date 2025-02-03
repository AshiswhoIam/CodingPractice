#underscore methods, auto called by py builtin op
#allow dev to def or customize obj behaviour

class Book:
    def __init__(self,title,author,num_pages):
        self.title=title
        self.author=author
        self.num_pages=num_pages


    def __str__(self):
        return f"'{ self.title }' by {self.author}"
    
    def __eq__(self, other):
        return self.title==other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages<other.num_pages

    def __gt__(self, other):
        return self.num_pages>other.num_pages   

    def __add__(self, other):
        return self.num_pages+ other.num_pages

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key ):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key {key} was not found"
        

book1=Book("The Hobbit","J.R.R Tolkien", 310)
book2=Book("Harry potter and the philospher","Jk Rolwling", 223)
book3=Book("The lion King","Someone", 120)  
book4=Book("The lion King","Someone", 212)  


#this doesnt work return memo add so need str method print(book1)
# this doesnt work have to make eq method print(book1=book2)

print(book1)
print(book1==book2)
print(book3==book4)

print(book2<book3)
print(book2+book3)

print("lion" in book3)
print("lion" in book1)

print(book1['title'])
print(book1['author'])
print(book1['num_pages'])
print(book1['audio'])
