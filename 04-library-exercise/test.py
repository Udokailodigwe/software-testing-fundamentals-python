import unittest
from library import Book, Library


#Test case for book Init
class BookInitTestCase(unittest.TestCase):
    def test_init(self):
        book = Book("The Python", "Mr Author")
        self.assertEqual(book.title, "The Python")
        self.assertEqual(book.author, "Mr Author")
        self.assertEqual(book.copies, 1)
        self.assertEqual(book.available, 1)

    def test_init_with_parameter(self):
        book = Book("The Math", "Mr Math Author", copies=3, available=2)
        self.assertEqual(book.title, "The Math")
        self.assertEqual(book.author, "Mr Math Author")
        self.assertEqual(book.copies, 3)
        self.assertEqual(book.available, 2)

    def test_availability(self):
        book = Book("The English", "Mr English Author", available=0)
        self.assertFalse(book.is_available())

    def test_pretty_name(self):
        title = "The Physics"
        author = "Mr Physics Author"
        book = Book(title, author)
        self.assertEqual(book.pretty_name(), '"The Physics" by Mr Physics Author')

class BookBorrowTestCase(unittest.TestCase):
    title = "The Biology"
    author = "The Author"

    def test_borrow_positive(self):
        book = Book(self.title, self.author)
        expected = f'You have borrowed "{self.title}" by {self.author}'
        self.assertEqual(book.borrow(), expected)

    def test_borrow_negative(self):
        book = Book(self.title, self. author, copies=80, available=0)
        expected = f'You are unable to borrow this book, sorry!'
        self.assertEqual(book.borrow(), expected)
        self.assertEqual(book.available, 0)
        self.assertEqual(book.copies, 80)


# Library test case

class LibraryTestCase(unittest.TestCase):
    library = Library()

    def test_library_init(self):
        self.assertDictEqual(self.library.books_by_title, {})

    def test_add_new_book(self):
        new_book = Book("Thinking fast and slow", "Daniel")
        self.library.add_book(new_book)
        # check for proper title
        self.assertIn("Thinking fast and slow", self.library.books_by_title)
        self.assertEqual(self.library.books_by_title["Thinking fast and slow"], new_book)

    def test_add_existing_book(self):
        another_new_book = Book("Thinking fast and slow", "Daniel")
        self.library.add_book(another_new_book)
        # check duplicate book
        self.assertEqual(len(self.library.books_by_title), 1)

    def test_remove_existing_book(self):
        new_book = Book("Thinking fast and slow", "Daniel")
        self.library.add_book(new_book)
        self.library.remove_book(new_book)
        self.assertNotIn("Thinking fast and slow", self.library.books_by_title)
        self.assertEqual(len(self.library.books_by_title), 0)

    def test_remove_non_existing_book(self):
        non_existing_book = Book("No title", "No name")
        self.library.remove_book(non_existing_book)

    def test_status_negative(self):
        new_book = Book("Thinking fast and slow", "Daniel")
        another_new_book = Book("No title", "No author")
        self.library.add_book(new_book)
        self.assertFalse(self.library.check_book_status(another_new_book.title))

    def test_status_positive(self):
        new_book = Book("Thinking fast and slow", "Daniel")
        self.library.add_book(new_book)
        self.assertTrue(self.library.check_book_status(new_book.title))