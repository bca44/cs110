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


def print_list(a_list, name):
    # prints the name of the list and each item, each on a separate line

    print(f"{name}:")

    for i in a_list:
        print(f" - {i}")


def summary(list1, name1, list2, name2, message1, message2, message3):
    # prints list names, items, and a message
    # list order and message is based on length comparison

    if len(list1) > len(list2):
        print_list(list1, name1)
        print_list(list2, name2)
        print(message1)

    elif len(list2) > len(list1):
        print_list(list2, name2)
        print_list(list1, name1)
        print(message2)

    else:
        print_list(list1, name1)
        print_list(list2, name2)
        print(message3)


def main():
    fruits = get_list("Enter a Fruit: ")
    veggies = get_list("Enter a Vegetable: ")
    summary(fruits, "Fruits", veggies, "Vegetables", "You need more vegetables!",
                "You need more fruit!", "What a healthy balanced diet!")


if __name__ == '__main__':
    main()
