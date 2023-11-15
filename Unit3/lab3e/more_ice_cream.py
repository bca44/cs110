def get_tuple_list(text1, text2):
    # gets a list of tuples, ending with a blank line
    # uses given 'text' parameters as prompts for input

    a_list = []

    while True:
        element1 = input(text1)
        if element1 == "":
            break
        element2 = input(text2)

        a_list.append((element1, element2))
    return a_list


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


def ratings_for_flavor(ratings, requested_flavor):
    # sorts a list of tuples by common first elements, matching the second parameter given

    new_list = []

    for i in ratings:
        if i[0] == requested_flavor:
            new_list.append(i)
    return new_list


def get_average(ratings):
    # takes the average of the second elements of a list of tuples

    total = 0

    for i in ratings:
        total += int(i[1])

    return round(total / len(ratings), 1)


def print_info(ratings, flavor):
    # prints the name and average rating of a flavor

    average = get_average(ratings)
    print(f"The average rating for {flavor} is {average}.")


def main():
    print("Enter all the ice cream ratings. Enter an empty flavor to end.")
    ratings = get_tuple_list("Enter a flavor: ", "Enter a rating: ")
    print("Enter flavors to get info on, ending with a blank line.")
    flavors = get_list("Flavor: ")
    for flavor in flavors:
        new_ratings = ratings_for_flavor(ratings, flavor)
        print_info(new_ratings, flavor)


if __name__ == '__main__':
    main()
