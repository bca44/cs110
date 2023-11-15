def out_of_stock():
    """
    asks customer what's out of stock, until "" entered
    returns list of out of stock items
    """
    out_list = []

    print("What items are out of stock?")

    while True:

        out_item = input("Item: ").lower()

        if out_item == "":
            break

        out_list.append(out_item)

    return out_list


def get_list(out_list):
    """
    gets shopping list from customer, until "" entered
    if item entered is in out_list, informs that it's out of stock and prompts input again
    returns list of desired items
    """
    a_list = []

    print("What items would you like to purchase?")

    while True:

        shop_item = input("Item: ")

        if shop_item.lower() in out_list:
            print(f"I'm sorry, the item {shop_item.upper()} is out of stock.")
            shop_item = input("Item: ")

        elif shop_item == "":
            break

        a_list.append(shop_item)

    return a_list


def print_list(a_list):
    """
    gives item count
    lists items in shopping list
    """

    print(f"You have {len(a_list)} items:")

    for item in a_list:
        print(f"- {item}")


def main():
    out_list = out_of_stock()
    item_list = get_list(out_list)
    print_list(item_list)


if __name__ == "__main__":
    main()
