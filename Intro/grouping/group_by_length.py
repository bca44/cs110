def group_by_length(words):
    """
    Group a list of words by their length.

    words -> a list of strings

    returns a dictionary that maps a letter to a list of words
    """
    groups = {}
    for word in words:
        # key is the length of the word
        key = len(word)

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

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
    groups = group_by_length(words)
    print(groups)


if __name__ == '__main__':
    main()