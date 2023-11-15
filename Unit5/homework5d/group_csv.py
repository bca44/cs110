import sys
from string import punctuation


def read_lines(filename):
    with open(filename) as file:
        return file.read().strip(punctuation).split()


def extract_column(tuple_list, column_number):
    # returns a list of the {column_number} value of each tuple
    column_list = []
    for element in tuple_list:
        element = element.split(",")
        column_list.append(element[column_number])

    return column_list


def make_dict(key_list, value_list):
    # makes a dictionary out of given keys and values
    # groups by common keys
    a_dict = {}

    for key, value in zip(key_list, value_list):
        if key not in a_dict:
            a_dict[key] = []
        a_dict[key].append(value)

    return a_dict


def main(input_file, key_column, value_column):
    # reads in CSV with name, grade1, grade2 columns
    # makes dict, using key_column as keys and value_column as values
    lines = read_lines(input_file)
    keys = extract_column(lines, key_column)
    values = extract_column(lines, value_column)
    dictionary = make_dict(keys, values)
    for key, values in dictionary.items():
        print(f"{key}: {values}")


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

# TODO: fails test, no way of knowing why.
# passes every scenario I have, everything on the hw
