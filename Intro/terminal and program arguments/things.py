import sys


def get_things(how_many, thing):
    """
    gets as many items as count given
    """

    things = []

    while how_many > len(things):
        item = input(f"{thing}: ")
        things.append(item)

    return things


def print_things(things):
    """
    prints each element in the list given
    """
    for thing in things:
        print(f"- {thing}")


def main():
    things = get_things(int(sys.argv[1]), sys.argv[2])
    print()
    print_things(things)


if __name__ == '__main__':
    main()
