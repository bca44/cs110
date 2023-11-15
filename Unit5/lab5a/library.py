def who_is_this_book_by(library, title):
    """
    Finds the author of a book in the library, given its title.
    'library' -- a dictionary mapping title to author
    'title' -- a string

    Prints:
    {title} is by {author}
    """
    print(f"{title} is by {library[title]}")


def do_you_have_these_books(library, books):
    """
    Checks whether the library has a given title.
    'library' -- a dictionary mapping title to author
    'books' -- a list of strings, each of which is a title.

    For each book, it prints either:
    Yes, we have {title} by {author}.
    or
    No, we don't have {title}, sorry!
    """

    for book in books:
        if book in library:
            print(f"Yes, we have {book} by {library[book]}.")
        else:
            print(f"No, we don't have {book}, sorry!")


def what_books_do_you_have_by(library, requested_author):
    """
    Prints the books the library has by a given author.
    'library' -- a dictionary mapping title to author
    'requested_author' -- a string

    Prints
    We have the following books by {author}:
    and then a bulleted list:
    * {title}
    """

    requested_author_list = []

    for title, author in library.items():
        if author == requested_author:
            requested_author_list.append(title)

    print(f"We have the following books by {requested_author}:")
    for title in requested_author_list:
        print(f"* {title}")


def main():
    library = {'In Search of Lost Time': 'Marcel Proust',
               'Ulysses': 'James Joyce',
               'Don Quixote': 'Miguel de Cervantes',
               'One Hundred Years of Solitude': 'Gabriel Garcia Marquez',
               'The Great Gatsby': 'F. Scott Fitzgerald',
               'Moby Dick': 'Herman Melville',
               'War and Peace': 'Leo Tolstoy',
               'Hamlet': 'William Shakespeare',
               'The Odyssey': 'Homer',
               'Madame Bovary': 'Gustave Flaubert',
               'The Divine Comedy': 'Dante Alighieri',
               'Lolita': 'Vladimir Nabokov',
               'The Brothers Karamazov': 'Fyodor Dostoyevsky',
               'Crime and Punishment': 'Fyodor Dostoyevsky',
               'Wuthering Heights': 'Emily Brontë',
               'The Catcher in the Rye': 'J. D. Salinger',
               'Pride and Prejudice': 'Jane Austen',
               'The Adventures of Huckleberry Finn': 'Mark Twain',
               'Anna Karenina': 'Leo Tolstoy',
               'Alice\'s Adventures': 'Wonderland by Lewis Carroll',
               }
    who_is_this_book_by(library, 'Pride and Prejudice')
    do_you_have_these_books(library, ['Pride and Prejudice',
                                      'Invisible Man',
                                      'Anna Karenina',
                                      'To Kill a Mockingbird'])
    what_books_do_you_have_by(library, 'Fyodor Dostoyevsky')


if __name__ == '__main__':
    main()
