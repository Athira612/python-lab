class publisher:
    def title(self):
        print("title of book")
    def author(self):
        print("author of the book::")
class book(publisher):
    def title(self):
        print("book name is python:")
    def price(self):
        print("price of the book::559")
    def no_of_page(self):
        print("bno_og_page:850")
obj=book()
obj.title()
obj.author()
obj.price()
obj.no_of_page()