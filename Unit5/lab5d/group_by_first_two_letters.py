def group_by_first_two_letters(words):
    """
    Group a list of words by their first two letters.

    words -> a list of strings

    returns a dictionary that maps a letter to a list of words
    """
    two_letters_dict = {}

    for word in words:
        key = word[0:2]

        if key not in two_letters_dict:
            two_letters_dict[key] = []

        two_letters_dict[key].append(word)

    return two_letters_dict


def get_words():
    """
    Get a list of words from input
    """
    words = []
    while True:
        word = input("Word: ")
        if word == "":
            break
        words.append(word)

    return words


def main():
    words = get_words()
    print(words)
    groups = group_by_first_two_letters(words)
    print(groups)


if __name__ == '__main__':
    main()
