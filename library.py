import sys
# Описать класс «домашняя библиотека».
# Предусмотреть возможность работы с произвольным числом книг, поиска книги по какому-либо признаку (например, по автору или по году издания),
# добавления книг в библиотеку, удаления книг из нее, сортировки книг по разным полям.

class Home_library:
    def __init__(self, author, name, year):
        self.name = name
        self.author = author
        self.year = year

    def __str__(self):
        return str(self.__dict__)


list_of_books = [Home_library(b[0], b[1], b[2]) for b in [
    ("John Doe", "Lost Planet", 1982),
    ("Jane Doe", "Fallen angels", 1890),
    ("Alan Smith", 'All done, all gone', 1985),
    ("Clint Eastwood", "The good, the bad and the ugly", 1956),
    ("Alan Smith", 'Alien pursuit', 1991),
    ('Mary Shelly', "Frankenstein", 1890)
]]


def year_definition(list_of_books, year):
    for book in list_of_books:
        if book.year == year:
            yield book

needed_book = str(input("Enter book's name: "))
method = input('Enter the method you want to sort by (by "name", by "book", by "author"): ')
selected_method = f"{'bookz.'}{method}"
year_of_book = int(input('Enter the year of book you would like to find: '))
year_of_book = str(year_of_book)
if len(year_of_book) != 4:
    print("Enter appropriate year format!")
    sys.exit()
else:
    year_of_book = int(year_of_book)


class Interaction:

    def __init__(self, user):
        self.user = user

    def select_by_year(self, year_of_book):
        for book in year_definition(list_of_books, year_of_book):
            print(book)

    def all_books(self):
        for book in list_of_books:
            print(book)

    def Author(self, findable):
        for book in list_of_books:
            if findable in book.author:
                print(book)


    def select_book_by_name(self, findable2):
        for book in list_of_books:
            if findable2 in book.name:
                print(book)

    @staticmethod
    def sorting():
        method = input('Enter the method you want to sort by (by "name", by "book", by "author"): ')
        selected_method = f"{'bookz.'}{method}"
        for bookz in sorted(list_of_books, key=lambda bookz: selected_method):
            print(bookz)

    @staticmethod
    def add_book_to_library():

        bookname = input("Add book name: ")
        authorname = input("Add author name: ")
        addyear = input("Enter year of the book: ")

        result = ['name', bookname, 'author', authorname, 'year', addyear]
        dicted = {item: result[index + 1] for index, item in enumerate(result) if
                    index % 2 == 0}  # converts to dict
        list_of_books.append(dicted)





Al_Mualim = Interaction('Al Mualim')
Altair = Interaction('Altair')

Al_Mualim.add_book_to_library()
Altair.all_books()



#Al_Mualim.add_book_to_library()
# Al_Mualim.select_book_by_name(needed_book)
# Al_Mualim.select_by_year(year_of_book)

# Al_Mualim.sorting()

#Al_Mualim.all_books()
# print("\n")
#Al_Mualim.Author("Doe")
# print("\n")
# Al_Mualim.add_book_to_library()
# print("\n")
# Al_Mualim.all_books()

# Al_Mualim.year_definition(list_of_books, year)
# Al_Mualim.select_by_year(year_definition)
