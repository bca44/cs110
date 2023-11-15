import sys


def get_word_list(min_length):
    """
    gets a list of 5 words
    only accepts input words with length >= min_length
    otherwise, says "too short"
    """
    word_list = []

    while 5 > len(word_list):
        word = input("Word: ")

        if len(word) >= int(min_length):
            word_list.append(word)
        else:
            print("Too short.")

    return word_list


def print_list(a_list):
    """
    prints each word in list with a leading hyphen
    """
    for item in a_list:
        print(f"- {item}")


def main(sys_arg):
    word_list = get_word_list(sys_arg)
    print_list(word_list)


if __name__ == "__main__":
    main(sys.argv[1])
