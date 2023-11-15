def get_list():
    # takes input, stores in 'list'
    # stops when "" entered
    list = []

    while True:
        word = input("Word: ")

        if word == "":
            break

        list.append(word)
    return list


def get_boundary():
    # takes user's boundary word and returns it
    return input("Boundary: ")


def print_number(list):
    # prints number of elements in list

    word_count = len(list)
    print(f"You have {word_count} words")


def print_before(list, boundary):
    # gives 'small words,' or words that come before 'boundary' alphabetically
    print("These are small:")
    for word in list:
        if word < boundary:
            print(word)


def print_after(list, boundary):
    # gives 'big words,' or words that come after 'boundary' alphabetically
    print("These are big:")
    for word in list:
        if word > boundary:
            print(word)


def main():
    word_list = get_list()
    boundary = get_boundary()
    print_number(word_list)
    print_before(word_list, boundary)
    print_after(word_list, boundary)


if __name__ == '__main__':
    main()
