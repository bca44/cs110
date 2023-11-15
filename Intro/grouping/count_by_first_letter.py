def count_by_first_letter(words):
    """
    Count a list of words by their first letter.

    words -> a list of strings

    returns a dictionary that maps a letter to a count
    """
    # create an empty dictionary to map letters to lists of words
    counts = {}
    for word in words:
        # define the key, which in this case is the first letter of the word
        key = word[0]

        # initialize the key to zero if it is not in the dictionary
        if key not in counts:
            counts[key] = 0

        # add 1
        counts[key] += 1

    # return the dictionary
    return counts


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
    counts = count_by_first_letter(words)
    print(counts)


if __name__ == '__main__':
    main()