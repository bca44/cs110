def get_items():
    # takes items from user, adds to items list
    # if item == " ", breaks

    items = []
    while True:

        response = input('Enter an item: ')

        if response == '':
            break

        items.append(response)

    return items


def main():

    shopping_list = get_items()
    print(shopping_list)


if __name__ == '__main__':
    main()
