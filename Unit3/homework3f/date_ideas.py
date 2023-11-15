def get_tuple_list(text1, text2):
    # gets a list of tuples, ending with a blank line
    # uses given 'text' parameters as prompts for input
    # ends collection when element1 ""

    a_list = []

    while True:
        element1 = input(text1)
        if element1 == "":
            break
        element2 = int(input(text2))

        a_list.append((element1, element2))
    return a_list


def single_list(a_list, max_cost):
    #
    return [(idea, cost) for idea, cost in a_list if cost <= max_cost]


def summary(a_list, max_value):
    #
    print(f"Here are all the dates below ${max_value}:")

    [print(f"- {idea} costs ${cost}.") for idea, cost in a_list]


def main():
    idea_list = get_tuple_list("Date idea: ", "Date cost: ")
    max_cost = int(input("Get max cost for date: "))
    below_max_list = single_list(idea_list, max_cost)
    summary(below_max_list, max_cost)


if __name__ == '__main__':
    main()
