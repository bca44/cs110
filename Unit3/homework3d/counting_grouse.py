def get_list(text):
    # gets a list, ending with a blank line
    # uses given 'text' parameter as prompt for input

    a_list = []

    while True:
        item = input(text)
        if item == "":
            break

        a_list.append(int(item))
    return a_list


def get_min(input_list):
    # finds smallest element in provided list
    # initializes 'smallest' as first item, will replace it next is smallest

    smallest = input_list[0]

    for element in input_list:
        if element < smallest:
            smallest = element
    print(f"The smallest count is: {smallest}")


def get_max(input_list):
    # finds largest element in provided list
    # initializes 'largest' as first item, will replace it

    largest = input_list[0]

    for element in input_list:
        if element > largest:
            largest = element
    print(f"The largest count is: {largest}")


def estimate_populations(input_list, factor):
    estimates = [i * factor for i in input_list]
    print("The estimated grouse populations are:")
    [print(f"- {i}") for i in estimates]


def sum_total(input_list):
    print(f"There are {sum(element for element in input_list)} total grouse.")


def main():
    counts = get_list("Enter an observation count: ")
    sum_total(counts)
    get_min(counts)
    get_max(counts)
    factor = int(input("Enter factor: "))
    estimate_populations(counts, factor)


if __name__ == '__main__':
    main()
