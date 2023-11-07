n = 5 

for i in range(n):
    for j in range(i+1):
        print(j+1, end=" ")
    print()


"""
* 
* * 
* * *
* * * *
* * * * *
"""

class book_shop:

    # constructor
    def __init__(self, title):
        self.title = title

    # Sample method
    def book(self):
        print('The tile of the book is', self.title)


b = book_shop('Sandman')
b.book()
# The tile of the book is Sandman


class Monkey:
    def patch(self):
          print ("patch() is being called")

def monk_p(self):
    print ("monk_p() is being called")

# replacing address of "patch" with "monk_p"
Monkey.patch = monk_p

obj = Monkey()

obj.patch()
# monk_p() is being called



