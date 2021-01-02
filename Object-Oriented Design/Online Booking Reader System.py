"""Online booking reader system

Start program and use command line.

"""

# from absl import app


class OnlineBookingReaderSystem:

    from enum import Enum

    class Status(Enum):
        READING = "READING"
        EXIT = "EXIT"

    # class Subscription(Enum):
    #     BASIC = "BASIC"
    #     PREMIUM = "PREMIUM"

    class SystemState(Enum):
        EXIT_THE_SYSTEM = 0
        GET_INTO_THE_SYSTEM = 1
        READER_IN_THE_SYSTEM = 2
        MANAGER_IN_THE_SYSTEM = 3

    class UserResponseAction(Enum):
        READ = "Read"
        CHECK = "Check"
        ADD = "Add"
        REMOVE = "Remove"
        EXIT = "Exit"

    class UserResponseObject(Enum):
        BOOK = "book"
        CATEGORY = "category"

    def __init__(self, max_books_number: int):
        self.reader_database = self.ReadersDatabase()
        self.books_database = self.BooksDatabase(max_books_number)
        self.reader_database.add_manager(self.Manager("Manager", self.books_database))
        self.initial_books_database()

    def initial_books_database(self):
        books = [
            "Drama, The Pit, [sometext1, sometext2, sometext3, sometext4, sometext5]",
            "Drama, Casino, [sometext1, sometext2, sometext3, sometext4, sometext5]",
            "Comedy, Are you crazy?, [sometext1, sometext2, sometext3, sometext4, sometext5]",
            "Science, Human Brain, [sometext1, sometext2, sometext3, sometext4, sometext5]",
            "Science, Physics, [sometext1, sometext2, sometext3, sometext4, sometext5]",
            "Historical, World Wars, [sometext1, sometext2, sometext3, sometext4, sometext5]"
        ]
        for book_data in books:
            book_info = convert_book_string_to_data(book_data)
            book = self.Book(book_info[0], book_info[1], book_info[2])
            self.books_database.add_book(book)

    def input(self):

        print("\n")
        user_name = "Manager"

        self.print_initial_instruction()
        current_state = self.SystemState.GET_INTO_THE_SYSTEM
        while current_state != self.SystemState.EXIT_THE_SYSTEM:

            if current_state == self.SystemState.GET_INTO_THE_SYSTEM:
                user_name = self.get_user_name_from_console()
                if user_name == self.UserResponseAction.EXIT.value:
                    current_state = self.SystemState.EXIT_THE_SYSTEM
                    break
                if user_name not in self.reader_database.readers_database:
                    print("User with that name is not in our database")
                    print("Do you want to create new one?")
                    if self.get_users_response_yes_no():
                        new_user = self.Reader(user_name, self.books_database)
                        self.reader_database.add_reader(new_user)
                        current_state = self.SystemState.READER_IN_THE_SYSTEM
                    else:
                        continue
                else:
                    if user_name == "Manager":
                        for count in range(3, 0, -1):
                            user_password = self.get_user_password()
                            password = "admin123"
                            if user_password == password:
                                current_state = self.SystemState.MANAGER_IN_THE_SYSTEM
                                break
                            else:
                                print("Wrong password. Try again. You have ", count-1, " more tries")
                        if current_state != self.SystemState.MANAGER_IN_THE_SYSTEM:
                            print("Try again\n")
                    else:
                        current_state = self.SystemState.READER_IN_THE_SYSTEM

            if current_state == self.SystemState.MANAGER_IN_THE_SYSTEM:
                self.print_reader_instruction()
                self.print_manager_instruction()
                user = self.reader_database.get_reader(user_name)
                user_input = ""
                while True:
                    user_input = input()

                    # read_1 = user_input[:len(self.UserResponseAction.READ.value)]
                    # read_vs = self.UserResponseAction.READ.value
                    #
                    # check_1 = user_input[:len(self.UserResponseAction.CHECK.value)]
                    # check_vs = self.UserResponseAction.CHECK.value
                    # check_1_1 = user_input[10:10+len(self.UserResponseObject.BOOK.value)]
                    # check_1_vs = self.UserResponseObject.BOOK.value
                    #
                    # add_1 = user_input[:len(self.UserResponseAction.ADD.value)]
                    # add_vs = self.UserResponseAction.ADD.value
                    # add_category = user_input[8:8+len(self.UserResponseObject.CATEGORY.value)]
                    # add_book = user_input[8:8+len(self.UserResponseObject.BOOK.value)]

                    # read operation
                    if user_input[:len(self.UserResponseAction.READ.value)] \
                            == self.UserResponseAction.READ.value:
                        book_name = user_input[len("Read the book "):]
                        user.read_book(book_name)
                        continue
                    # exit operation
                    elif user_input[:len(self.UserResponseAction.EXIT.value)] \
                            == self.UserResponseAction.EXIT.value:
                        print("You exit from the Manager mode")
                        current_state = self.SystemState.GET_INTO_THE_SYSTEM
                        break
                    # check operation
                    elif user_input[:len(self.UserResponseAction.CHECK.value)] \
                            == self.UserResponseAction.CHECK.value:
                        # len("Check all ") => 10
                        if user_input[10:10+len(self.UserResponseObject.BOOK.value)] == \
                                self.UserResponseObject.BOOK.value:
                            # self.get_list_of_books() will print them out
                            all_books_in_database = self.get_list_of_books()
                        else:
                            print("Wrong command. Try again")
                        continue
                    # add operation
                    elif user_input[:len(self.UserResponseAction.ADD.value)] \
                            == self.UserResponseAction.ADD.value:
                        # add category
                        if user_input[8:8+len(self.UserResponseObject.CATEGORY.value)] \
                                == self.UserResponseObject.CATEGORY.value:
                            category_name = \
                                user_input[9+len(self.UserResponseObject.CATEGORY.value):]
                            self.books_database.add_category(category_name)
                        # add book
                        elif user_input[8:8+len(self.UserResponseObject.BOOK.value)] \
                                == self.UserResponseObject.BOOK.value:
                            book_data = user_input[14:]
                            book_info = convert_book_string_to_data(book_data)
                            book = self.Book(book_info[0], book_info[1], book_info[2])
                            self.books_database.add_book(book)
                        else:
                            print("Wrong command. Try again")
                            continue
                    # remove
                    elif user_input[:len(self.UserResponseAction.REMOVE.value)] \
                            == self.UserResponseAction.REMOVE.value:
                        if user_input[11:11+len(self.UserResponseObject.BOOK.value)] \
                                == self.UserResponseObject.BOOK.value:
                            book_name = user_input[11+len(self.UserResponseObject.BOOK.value)+1:]
                            self.books_database.remove_book(book_name)
                        elif user_input[11:11+len(self.UserResponseObject.CATEGORY.value)] \
                                == self.UserResponseObject.CATEGORY.value:
                            category_name = user_input[11+len(self.UserResponseObject.CATEGORY.value)+1:]
                            self.books_database.remove_category(category_name)
                        else:
                            print("Wrong command. Try again")
                            continue
                    else:
                        print("Wrong command. Try again")
                        continue

            if current_state == self.SystemState.READER_IN_THE_SYSTEM:
                self.print_reader_instruction()
                user = self.reader_database.get_reader(user_name)
                user_input = ""
                while True:

                    user_input = input()

                    # read operation
                    if user_input[:len(self.UserResponseAction.READ.value)] \
                            == self.UserResponseAction.READ.value:
                        book_name = user_input[len("Read the book "):]
                        user.read_book(book_name)
                        continue
                    # exit operation
                    elif user_input[:len(self.UserResponseAction.EXIT.value)] \
                            == self.UserResponseAction.EXIT.value:
                        print("You exit from the reader mode")
                        current_state = self.SystemState.GET_INTO_THE_SYSTEM
                        break
                    # check operation
                    elif user_input[:len(self.UserResponseAction.CHECK.value)] \
                            == self.UserResponseAction.CHECK.value:
                        # len("Check all ") => 9
                        if user_input[10:10+len(self.UserResponseObject.BOOK.value)] == \
                                self.UserResponseObject.BOOK.value:
                            # self.get_list_of_books() will print them out
                            all_books_in_database = self.get_list_of_books()
                        continue
                    else:
                        print("Wrong command. Try again")
                        continue

        print("Have a good day")

    def get_list_of_books(self, category=None):
        list_of_books = self.books_database\
            .get_list_of_books(category)
        # pagination?
        return list_of_books

    def get_list_of_readers(self):
        return self.reader_database.get_list_of_readers()

    def print_initial_instruction(self):
        print("Welcome to Online Booking Reader System")
        print("Take a note: type 'Exit' to exit the application")

    def get_user_name_from_console(self):
        print("Enter your name: ")
        user_name = input()
        return user_name

    def get_users_response_yes_no(self):
        print("Enter 'yes'/'no': ")
        user_response = input()
        return user_response == "yes"

    def get_user_password(self):
        print("password: ")
        password = input()
        return password

    def print_reader_instruction(self):
        print("List of commands are listed below:")
        print("     Check all books' list")
        print("     Read the book XXXXX")
        print("     Exit")
        # print("Add the book XXXXX to wish list")
        # print("Check books in your wish list")
        # print("Check books in progress")
        # print("Check your completed books")

    def print_manager_instruction(self):
        print("     Add new category XXXXX")
        print("     Add new book: category, name, text")
        print("         Example of new book: "
              "     Add new book: Drama, The Pit, [page1, page2]")
        print("     Remove the book XXXXX")
        print("     Remove the category XXXXX")

    class BooksDatabase:
        """
        .add_category(category: str)
        .add_book(book: Book)
        .add_book_to_category(book: Book, category: str)
        .get_book(book_name: str) -> Book()
        .remove_book(book_name: str)
        .get_books_database_fullness() -> int
        .remove_category(category: str)
        .get_category_statistics() -> list
        .get_list_of_books(category?: str) -> list
        """
        def __init__(self, books_limit: int):
            self.books_database = {}
            self.books_limit = books_limit
            self.books_in_database = 0

        def add_category(self, category):
            if category not in self.books_database:
                self.books_database[category] = {}
                print("Category \"", category,
                      "\" was added successfully")

        def add_book(self, book):
            category = book.category
            if self.get_books_database_fullness() != 100:
                self.add_category(category)
                self.add_book_to_category(book, category)
                self.books_in_database += 1
                print("Books database is full on",
                      self.get_books_database_fullness(), "%")
                # print("Book", book.name, "was added successfully")
            else:
                print("Books database is full")

        def add_book_to_category(self, book, category):
            if self.get_books_database_fullness() != 100:
                self.books_database[category][book.name] = book
                self.books_in_database += 1
                print("Book", book.name,
                      "was added to category",
                      category, "successfully")
            else:
                print("Books database is full")

        def get_book(self, book_name: str):
            for category in self.books_database:
                if book_name in self.books_database[category]:
                    print("Book", book_name,
                          "was found successfully")
                    book = self.books_database[category][book_name]
                    return book
            # print("There is no such book")
            return None

        def remove_book(self, book_name):
            book_to_remove = self.get_book(book_name)
            if book_to_remove is not None:
                del self.books_database[book_to_remove.category][book_name]
                print("Book", book_name,
                      "was removed successfully")
                self.books_in_database -= 1

        def get_books_database_fullness(self):
            fullness = self.books_in_database * 100 // self.books_limit
            return fullness

        def remove_category(self, category):
            if category in self.books_database:
                if len(self.books_database[category]):
                    print("There are some books in this category")
                    print("Do you want to delete this category with all books there?")
                    print("Type 'yes'/'no'")
                    users_response = input()
                    if users_response == 'y' or users_response == 'yes':
                        del self.books_database[category]
                        print("Category", category,
                              "was removed successfully")
                    else:
                        "Then let this category be"
            else:
                print("There is no such category")

        def get_category_statistics(self):
            statistics = []
            for category in self.books_database:
                category_statistic = category, "has", \
                                     len(self.books_database[category]), \
                                     "books"
                statistics.append(category_statistic)
                print(category_statistic)
            return statistics

        def get_list_of_books(self, category=None):
            books_list = []
            if category is None:
                for category in self.books_database:
                    for book_name in self.books_database[category]:
                        book_line_list = [category, book_name]
                        books_list.append(book_line_list)
                        print("Category", category,
                              "- Book", book_name)
            else:
                print("In category", category, " ",
                      len(self.books_database[category]), "books total")
                for book_name in self.books_database[category]:
                    book_line_list = [category, book_name]
                    books_list.append(book_line_list)
                    print("Book", book_name)
            if not len(books_list):
                print("There are no books in the system")
            return books_list

    class Book:
        """
        Book data.
        Book_text can be string, or list of strings
        """
        def __init__(self, category: str, name: str,
                     book_text):
            self.pages = len(book_text)
            self.category = category
            self.text = book_text
            self.name = name

        def read_page(self, page=0):
            page_text = None
            if 0 <= page < len(self.text):
                page_text = self.text[page]
                # print(page_text)
            else:
                page_text = "The END" if not page < 0 else "Wrong page"
            return page_text

    class Reader:
        """
        .read_book(book name: str) -> get book
        and start reading
        .add_book_to_wish_list(book name: str)
        .get_list_wish_list()
        .get_list_completed_list()
        .get_list_in_progress_list():
        """

        READING = "READING"
        EXIT = "EXIT"

        class _Collection:
            def __init__(self):
                """
                Example:
                    in_progress = {
                        "book name":
                            [Book(),
                            # of page where stopped to read],
                        ...
                """
                self.in_progress_list = {}
                self.completed_list = {}
                self.wish_list = {}

        def __init__(self, name: str, online_book_reading_system):
            self.name = name
            self.own_collection = self._Collection()
            # self.subscription =
            self.current_book = None
            self.respective_online_book_reading_system \
                = online_book_reading_system

        def open_book(self, book):
            if self.current_book is not None:
                self.close_book()
            self.current_book = book

        def close_book(self):
            self.current_book = None
            pass

        def read_book(self, book_name):
            if book_name in self.own_collection.in_progress_list:
                book, open_at_page = \
                    self.own_collection.in_progress_list[book_name]
                open_at_page -= 1
            elif book_name in self.own_collection.wish_list:
                book, open_at_page = \
                    self.own_collection.wish_list[book_name], 0
                del self.own_collection.wish_list[book_name]
                self.own_collection.in_progress_list[book_name] = [book, 0]
            else:
                if book_name in self.own_collection.completed_list:
                    del self.own_collection.completed_list[book_name]
                book = self.respective_online_book_reading_system.get_book(book_name)
                # check if the book is PREMIUM / BASIC
                # pass
                if book is None:
                    print("There is no such book in our database")
                    return
                self.own_collection.in_progress_list[book_name] = [book, 0]
                open_at_page = 0
            self.open_book(book)

            print("You started reading ", book_name, "at page ", open_at_page+1)
            print("To change a page, press ENTER")
            print("Type 'Move to page XXX' and press ENTER to move to that XXX page")
            print("To finish reading, write 'EXIT' and press ENTER")

            page = open_at_page-1
            while True:
                page += 1
                print("Page", page+1)
                text = book.read_page(page)
                print(text)
                if text == "The END":
                    del self.own_collection.in_progress_list[book.name]
                    self.own_collection.completed_list[book.name] = book
                    print("You completed reading the book")
                    break
                status = input()
                self.own_collection.in_progress_list[book.name][1] += 1
                if status == self.EXIT:
                    print("Type next command:")
                    break
                string_data = convert_string_to_data(status)
                if string_data[0] == 'Move':
                    if string_data[2] == 'page':
                        page = string_data[-1]
                        page = int(page)-2
                        self.own_collection.in_progress_list[book.name][1] = page+1
            self.close_book()

        def add_book_to_wish_list(self, book_name):
            self.own_collection.wish_list[book_name] = \
                self.respective_online_book_reading_system.get_book[book_name]
            print("Book ", book_name, " was added to your wish list")

        def get_list_wish_list(self):
            list_of_wish_books = []
            print("In your wish list")
            for wish in self.own_collection.wish_list:
                list_of_wish_books.append(wish)
                print(wish)
            return list_of_wish_books

        def get_list_in_progress_list(self):
            list_of_in_progress_books = []
            print("Started books")
            for book_name in self.own_collection.in_progress_list:
                book, page_at = self.own_collection.in_progress_list[book_name]
                list_of_in_progress_books.append([book_name, page_at])
                print(book_name, " at page ", page_at)
            return list_of_in_progress_books

        def get_list_completed_list(self):
            list_of_completed_books = []
            print("Completed books")
            for book_name in self.own_collection.completed_list:
                list_of_completed_books.append(book_name)
                print(book_name)
            return list_of_completed_books

    class Manager(Reader):
        """
        Manager is the guy who can manage books' database,
        like to add, to remove books/categories from there
        """

        def add_book_to_books_database(self, book):
            self.respective_online_book_reading_system.add_book(book)

        def add_category_to_book_database(self, category):
            self.respective_online_book_reading_system.add_category(category)

        def remove_book_from_books_database(self, book_name):
            self.respective_online_book_reading_system.remove_book(book_name)

        def remove_category(self, category):
            self.respective_online_book_reading_system.remove_category(category)

    class ReadersDatabase:
        """
        .add_reader(reader: Reader())
        .remove_reader(reader_name: str)
        .get_list_of_readers() -> list
        .get_reader(reader_name: str) -> Reader()
        """

        def __init__(self):
            self.readers_database = {}

        def add_manager(self, manager):
            if "Manager" not in self.readers_database:
                self.readers_database["Manager"] = manager
                print("Manager was added")
            else:
                print("There is a manager")

        def add_reader(self, reader):
            if reader not in self.readers_database:
                self.readers_database[reader.name] = reader
                print(reader.name, " was added successfully")
            else:
                print("There is already such reader name")

        def remove_reader(self, reader_name):
            if reader_name in self.readers_database:
                del self.readers_database[reader_name]
                print(reader_name, " was removed successfully")
            else:
                print("There is no such reader name")

        def get_list_of_readers(self):
            readers_list = []
            for reader_name in self.readers_database:
                readers_list.append(reader_name)
                print(reader_name)
            return readers_list

        def get_reader(self, reader_name):
            return self.readers_database[reader_name]


# Support functions
def convert_book_string_to_data(book_string):
    """Convert string into meaningful book info
    :param book_string: Drama, Yama, [page1, page2]
    :return: Drama, Yama, [page1, page2]
    """

    def _find_text(_string):
        start_point = -1
        end_point = -1
        for idx in range(len(_string)):
            if _string[idx] == '[':
                start_point = idx
            if _string[idx] == ']':
                end_point = idx + 1
        if start_point > -1:
            text = _string[start_point+1:end_point-1]
            text = text.split(', ')
        else:
            print("Write book text in brackets []")
            text = -1

        return text, start_point

    def remove_spaces_before(word):
        idx = 0
        while word[idx] == ' ':
            idx += 1
        if word[0] == ' ':
            word = word[idx:]
        return word

    book_text, text_start = _find_text(book_string)
    category_and_name = book_string[:text_start-2]
    category_and_name = category_and_name.split(',')
    book_category = remove_spaces_before(category_and_name[0])
    book_name = remove_spaces_before(category_and_name[1])
    return book_category, book_name, book_text


def convert_string_to_data(string):
    string_data = string.split(' ')
    return string_data


MAX_BOOKS_IN_ONLINE_BOOKING_READER = 100


def main():
    online_booking_reading_system = \
        OnlineBookingReaderSystem(MAX_BOOKS_IN_ONLINE_BOOKING_READER)
    online_booking_reading_system.input()


if __name__ == '__main__':
    # app.run(main)
    main()
    
