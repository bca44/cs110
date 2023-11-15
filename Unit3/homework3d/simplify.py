def get_list(text):
    # gets a list, ending with a blank line
    # uses given 'text' parameter as prompt for input

    a_list = []

    while True:
        item = input(text)
        if item == "":
            break

        a_list.append(item)
    return a_list


def get_length():
    # gets length from user

    return int(input("Enter a length: "))


def short_list(words, max_length):
    # filter pattern: takes elements with len <= of the max_length param
    short_words = [i for i in words if len(i) <= max_length]

    # prints intro and elements of new list
    print(f"There are {len(short_words)} short words:")
    [print(f"- {i}") for i in short_words]


def main():
    words = get_list("Enter a word: ")
    max_length = get_length()
    short_list(words, max_length)


if __name__ == '__main__':
    main()
