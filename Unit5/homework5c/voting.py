import sys


def get_list(prompt):
    """
    gets user input until done
    returns list of stripped input strings
    """

    item_list = []

    while True:
        item = input(f"{prompt}: ")

        if item == "":
            return item_list

        item_list.append(item.strip())


def make_dict(item_list):
    """
    makes a dict from a given list
    key: each unique item string
    value: the count of each unique item string in the original list
    """
    a_dict = {}
    for item in item_list:
        if item not in a_dict:
            a_dict[item] = 0
        a_dict[item] += 1

    return a_dict


def main(prompt):
    # get user input for foods
    # store food name and count in a dictionary
    # when done with input, print dictionary
    food_list = get_list(prompt)
    food_dict = make_dict(food_list)
    print(food_dict)


if __name__ == "__main__":
    main(sys.argv[1])
