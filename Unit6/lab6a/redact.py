import sys


def read_lines(filename):
    """
    Read the file given by <filename> and return a list of lines.
    """
    with open(filename) as file:
        return file.readlines()


def print_words(words):
    """
    <words> -- list of words

    Take a list of words, convert it to a string with spaces in
    between each word, and print it.
    """
    contents = " ".join(words)
    print(contents)


def replace_words(words, replace):
    """
    <words> -- list of words
    <replace> -- a list of words to replace

    Goes through every word in <words>. If it finds a word
    that matches one of the words in <replace>, then it replaces
    that word with "REDACTED".
    """
    for i in range(len(words)):
        if words[i] in replace:
            words[i] = "REDACTED"
    return words


def main(infile):
    # set up the words we want redacted
    replace = ['Dr.', 'Bean', 'Page', 'Zappala']
    # read all the lines from a file
    lines = read_lines(infile)
    for line in lines:
        # split the line into words
        words = line.split()
        # find any of the words from <replace> that occur in
        # <words> and replace them with the string "REDACTED"
        replace_words(words, replace)
        # print the words
        print_words(words)


if __name__ == '__main__':
    # run this program on the command line
    # the first argument should be a file name
    main(sys.argv[1])
