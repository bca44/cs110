import sys
from string import punctuation


def read_lines(filename):
    with open(filename) as file:
        return file.readlines()


def group_by_length(string_list):
    """
    groups each word in string_list by word length
    creates dictionary defined with word_length:count
    """
    word_length_dict = {i: 0 for i in range(1, 21)}
    for string in string_list:
        string = string.split(" ")
        for word in string:
            # find length of word, without newline or punctuation
            length = len(word.strip("\n").strip(punctuation))
            # update count for length key
            word_length_dict[length] += 1
    return word_length_dict


def main(input_file):
    # reads input_file
    lines = read_lines(input_file)

    # makes and prints dictionary with word_length:count pairs
    word_length_dict = group_by_length(lines)
    print(word_length_dict)


if __name__ == '__main__':
    main(sys.argv[1])
