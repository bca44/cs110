import sys


def readfile(filename):
    with open(filename) as file:
        return file.read()


def count_words(content):
    """Count the number of each word in content.
    Ignore casing and punctuation."""
    # create an empty dictionary
    counts = {}
    # loop through all of the words, first converting to lowercase
    # and then splitting them using white space
    for word in content.lower().split():
        # strip any leading or trailing punctuation from the word
        word = word.strip('!?,."\'')
        # if the word is not in the dictionary,
        # initialize an entry to zero
        if word not in counts:
            counts[word] = 0
        # increment the count by one for this word
        counts[word] += 1
    # return the dictionary
    return counts


def main(filename):
    # read the file
    content = readfile(filename)
    # count how many times each word appears
    counts = count_words(content)
    # print the counts dictionary
    print(counts)


if __name__ == '__main__':
    main(sys.argv[1])
