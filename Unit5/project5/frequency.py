import sys


def read_lines(filename):
    with open(filename) as file:
        return file.readlines()


def find_counts(string_list):
    """
    returns dictionary with char: count pairs
    not case-sensitive; lowercase char stored as key
    """
    char_count = {}
    for string in string_list:
        for char in string:
            if char.lower() not in char_count:
                char_count[char.lower()] = 0
            char_count[char.lower()] += 1
    return char_count


def frequency_analysis(count_dict, string_list):
    """
    converts char counts into frequency percentages
    returns dictionary with char: frequency pairs
    """
    frequency_dict = {}
    # finds the total length of all strings in string_list
    string_length = sum([len(item) for item in string_list])

    for char in count_dict:
        # sets value at char in count_dict to char_count/total string length
        frequency_dict[char] = round(count_dict[char]/string_length, 3)
    return frequency_dict


def main(input_file):
    # reads input file
    lines = read_lines(input_file)

    # generates dictionary with char: count pairs
    count_dict = find_counts(lines)

    # converts char: count pairs to char: frequency pairs
    # where 'frequency' is percentage of whole
    frequency = frequency_analysis(count_dict, lines)

    # prints dictionary
    print(frequency)


if __name__ == '__main__':
    main(sys.argv[1])
