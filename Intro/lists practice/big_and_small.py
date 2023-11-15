def get_numbers():
    # gets numbers from user until 'q' is typed

    number_list = []

    while True:

        number = input("Number: ")

        if number == "q":
            break

        number_list.append(int(number))
    return number_list


def get_boundary():
    # gets 'boundary' number from user

    boundary = int(input("Boundary: "))
    return boundary


def print_small(my_list, cutoff):
    # prints elements from list, if less than cutoff

    print("These are small:")

    for i in my_list:
        if i < cutoff:
            print(i)


def print_big(my_list, cutoff):
    # prints elements from list, if larger than cutoff

    print("These are big:")

    for i in my_list:
        if i > cutoff:
            print(i)


def main():

    number_list = get_numbers()
    cutoff = get_boundary()
    print_small(number_list, cutoff)
    print_big(number_list, cutoff)


if __name__ == '__main__':
    main()
