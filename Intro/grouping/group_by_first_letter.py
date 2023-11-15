def group_by_first_letter(words):
    """
    Group a list of words by their first letter.

    words -> a list of strings

    returns a dictionary that maps a letter to a list of words
    """
    # create an empty dictionary to map letters to lists of words
    groups = {}
    for word in words:
        # define the key, which in this case is the first letter of the word
        key = word[0]

        # initialize the key to an empty list if it is not in the dictionary
        if key not in groups:
            groups[key] = []

        # add this word to the list of words
        groups[key].append(word)

    # return the dictionary
    return groups


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
    groups = group_by_first_letter(words)
    print(groups)


if __name__ == '__main__':
    main()
