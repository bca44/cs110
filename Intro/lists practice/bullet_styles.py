def get_list():
    # gets items from user, until user enters "q"
    # adds to my_list and returns it

    my_list = []
    list_item = " "

    while True:
        list_item = input("Item: ")

        if list_item == "q":
            break

        my_list.append(list_item)

    return my_list


def print_individual(list, bullet):
    for i in list:
        print(f"{bullet} {i}")
    print()


def main():
    my_list = get_list()
    print_individual(my_list, "*")
    print_individual(my_list, "-")
    print_individual(my_list, "<")


if __name__ == '__main__':
    main()
