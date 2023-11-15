def get_tuple_list(text1, text2, text3):
    # gets a list of tuples, ending with a blank line
    # uses given 'text' parameters as prompts for input
    # ends collection when element1 ""

    a_list = []

    while True:
        element1 = input(text1)
        if element1 == "":
            break
        element2 = input(text2)
        element3 = input(text3)

        a_list.append((element1, element2, element3))
    return a_list


def one_author_list(text, tuple_list):
    # gives summary of book list
    # filter pattern: finds tuples with same author as given input

    response = input(text)

    one_author = [i for i in tuple_list if i[1] == response]
    return one_author


def author_summary(a_list):
    # gives summary of a list of tuples
    # gives author (tuple[1])
    # gives total book count (len(list))
    # gives total page count (sum of all tuple[2])

    title, author, pages = a_list[0]

    number_books = len(a_list)

    page_total = 0
    for i in a_list:
        page_total += int(i[2])

    print(f"You have read {number_books} books by {author}.")
    print(f"You have read {page_total} pages by {author}.")


def main():
    print("Enter the title, author, and pages of each book.")
    print("End with a blank title.")
    book_list = get_tuple_list("Title: ", "Author: ", "Pages: ")
    print("Enter an author to report on.")
    author_list = one_author_list("Author: ", book_list)
    author_summary(author_list)


if __name__ == '__main__':
    main()
