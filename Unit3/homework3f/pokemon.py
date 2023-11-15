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
        element3 = int(input(text3))

        a_list.append((element1, element2, element3))
    return a_list


def specific_list(a_list, a_type):
    # sort elements of a_list by first element
    # adds all tuples with first element == "a_type" to new list and returns it

    return [(name, TYPE, HP) for name, TYPE, HP in a_list if TYPE == a_type]


def find_largest(a_list):
    # compares the size element of each tuple, returns the 'largest' tuple

    largest_name, largest_type, largest_HP = (a_list[0])
    for place, fish_type, size in a_list:
        if size > largest_HP:
            largest_name, largest_type, largest_HP = place, fish_type, size
    return largest_name, largest_type, largest_HP


def summary(max_tuple):
    # prints max HP summary

    name, TYPE, HP = max_tuple
    print(f"{name} has the highest HP ({HP}) for type {TYPE}.")


def main():
    roster = get_tuple_list("Name: ", "Type: ", "HP: ")
    query_type = input("Get max HP for type: ")
    type_list = specific_list(roster, query_type)
    max_pokemon = find_largest(type_list)
    summary(max_pokemon)


if __name__ == '__main__':
    main()
