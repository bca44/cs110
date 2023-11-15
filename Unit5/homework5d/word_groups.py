import sys
from string import punctuation


def read_lines(filename):
    with open(filename) as file:
        return file.read().strip(punctuation).split()


def make_dict(string_list):
    # makes a dictionary of the string_list
    # sorts word elements by length and first letter, with tuples as keys
    length_letter_dict = {}

    for word in string_list:
        word = word.strip(punctuation)
        # if (first letter, length) not a key in dict:
        if (len(word), word[0].lower()) not in length_letter_dict:
            # add key, with an empty list as value
            length_letter_dict[(len(word), word[0].lower())] = []
        # add word string to entry at corresponding (first letter, length) key
        length_letter_dict[(len(word), word[0].lower())].append(word.lower())

    return length_letter_dict


def main(input_file):
    # reads in a file with words
    # groups words in a dict, with key: length, first letter
    words = read_lines(input_file)
    word_groups = make_dict(words)
    for group, words in word_groups.items():
        print(f"{group}: {words}")


if __name__ == "__main__":
    main(sys.argv[1])
