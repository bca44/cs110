import sys


def count(letters, text):
    # create an empty dictionary
    counts = {}

    # loop through all of the letters we are counting
    # and initialize their counts to zero
    for letter in letters:
        counts[letter] = 0

    # loop through all of the letters in the text
    # be sure to convert to lowercase
    for c in text.lower():
        # if this letter is one we are counting, add 1 to its count
        if c in counts:
            counts[c] += 1

    # return the dictionary
    return counts


def main(text):
    # count how many times each vowel occurs in the text
    vowel_counts = count('aeiou', text)
    # print out the dictionary
    print(vowel_counts)


if __name__ == '__main__':
    main(sys.argv[1])
