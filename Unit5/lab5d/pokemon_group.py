import sys


def readlines(filename):
    """ Read a file and return a list of lines. """
    with open(filename) as file:
        return file.readlines()


def group_pokemon(lines, column):
    """
    lines: a list of lines, each line is a comma-separated list of values
    column: an integer column number

    Find all of the Pokemon who have the same value in the given column.

    Return a dictionary that maps the column value to the list of Pokemon.
    For example, if the column is the number 4, then the dictionary will
    map the Pokemon type (water, fire) to a list of Pokemon of that type.
    """
    pokemon_dict = {}

    for line in lines:
        line = line.split(",")
        key = line[int(column)]

        if key not in pokemon_dict:
            pokemon_dict[key] = []

        pokemon_dict[key].append(line[0])

    return pokemon_dict


def print_groups(groups):
    """ Print a dictionary that maps words to a list of Pokemon . """
    for value, pokemon in groups.items():
        print(f"{value}")
        for name in pokemon:
            print(f"* {name}")


def main(filename, column):
    # read all the lines of the file
    lines = readlines(filename)
    # count the Pokemon of each type
    groups = group_pokemon(lines, column)
    print_groups(groups)


if __name__ == '__main__':
    main(sys.argv[1], int(sys.argv[2]))
