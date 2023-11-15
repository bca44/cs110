import sys


def read_lines(filename):
    with open(filename) as file:
        return file.readlines()


def count(string_list, index):
    """
    returns dict
    keys: unique items in specified column
    values: frequency of said item
    """
    count_dict = {}

    for string in string_list:
        string = string.split(",")
        item = string[index].strip()

        if item not in count_dict:
            count_dict[item] = 0
        count_dict[item] += 1

    return count_dict


def main(input_file, column_number):
    """
    reads in a CSV file with several columns
    column_number specifies which column is in question
    makes dictionary with each unique value in column and its frequency
    """
    lines = read_lines(input_file)
    count_dict = count(lines, column_number)
    print(count_dict)


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
