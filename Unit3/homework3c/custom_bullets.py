def get_list(text):
    # gets a list, ending with a blank line
    # uses given 'text' parameter as prompt for input

    list = []

    while True:
        item = input(text)
        if item == "":
            break

        list.append(item)
    print()
    return list


def print_bullet_list(list, bullet):
    # prints list multiple times, once with each type of bullet

    for item in bullet:

        for element in list:
            print(f"{item} {element}")

        print()


def main():
    list = get_list("Item: ")
    bullet = get_list("Custom Bullet Point: ")
    print_bullet_list(list, bullet)


if __name__ == '__main__':
    main()
