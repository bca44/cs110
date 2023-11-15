import random


def get_words():
    # returns two words input from user
    word1 = input("Word 1: ")
    word2 = input("Word 2: ")
    return word1, word2


def compare(string1, string2):
    # compares two strings
    # prints '*' for like characters, '.' for different

    result_list = []

    for char1, char2 in zip(string1, string2):
        if char1 == char2:
            result_list.append("*")
        else:
            result_list.append(".")

    print("".join(result_list))
    return "".join(result_list)


def main():
    # gets user input for two words
    # compares the two words
    # for each character, prints '*' if same, '.' if not

    while True:
        word1, word2 = get_words()
        if word1 == "":
            break
        compare(word1, word2)


if __name__ == '__main__':
    main()
