import sys
from string import punctuation


def read_line(filename):
    with open(filename) as file:
        return file.read()


def count_letters(count_word, txt_string):
    """
    Returns a dictionary with each letter in count_word and its frequency
    """
    count_dict = {}

    for letter in count_word:
        count_dict[letter] = 0

    for letter in txt_string.strip(punctuation):
        if letter.lower() in count_word:
            count_dict[letter.lower()] += 1

    return count_dict


def main(word, input_file):
    """
    reads an input file
    # for each letter in word, returns a dictionary
    # containing "letter: frequency" as found in input_file
    """
    input_string = read_line(input_file)
    count_dict = count_letters(word, input_string)
    print(count_dict)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
