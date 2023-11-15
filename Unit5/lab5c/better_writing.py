import sys
from string import punctuation


def readfile(filename):
    """ Read an entire file and return its contents as one long string. """
    with open(filename) as file:
        return file.read()


def count_words(content, words):
    """
    content -- a string
    words -- a list of strings

    Count how many times each word in <words> appears in <content>.
    Return a dictionary that maps each word in <words> to its count.
    """
    counts = {}
    for word in content.strip(punctuation).split(" "):

        # add key to dict and initialize count value to 0
        if word in words and word not in counts:
            counts[word] = 0
        # add occurrence to count value
        if word in counts:
            counts[word] += 1

    return counts


def print_counts(counts):
    """ Print a dictionary that maps words to counts. """
    for word, count in counts.items():
        print(f"{word}: {count}")


def main(filename):
    # read the file into a long string
    content = readfile(filename)
    # count how often "very" and "really" appear in the string
    counts = count_words(content, ['very', 'really'])
    # print the counts
    print_counts(counts)


if __name__ == '__main__':
    main(sys.argv[1])
