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

    return [(place, fish_type, size) for place, fish_type, size in a_list if fish_type == a_type]


def print_summary(a_list):
    # give total # of specified fish

    place, fish_type, size = a_list[0]
    print(f"Total # of {fish_type}: {len(a_list)}")

    # calculate best catch and print those details

    largest_place, largest_fish, largest_size = find_largest(a_list)
    print(f"Best {largest_fish} catch: {largest_size} inches at {largest_place}")


def find_largest(a_list):
    # compares the size element of each tuple, returns the 'largest' tuple

    largest_place, largest_type, largest_size = (a_list[0])
    for place, fish_type, size in a_list:
        if size > largest_size:
            largest_place, largest_type, largest_size = place, fish_type, size
    return largest_place, largest_type, largest_size

    # another option, more condensed and less intuitive
    # return max(a_list, key=lambda x: x[2])


def main():
    big_list = get_tuple_list("Place: ", "Type of fish: ", "Size (inches): ")
    single_list = specific_list(big_list, input("Fish type: "))
    print_summary(single_list)


if __name__ == '__main__':
    main()
