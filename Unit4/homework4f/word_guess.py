import sys
import random


def read_lines(filename):
    with open(filename) as file:
        return file.readlines()


def get_random_word(a_list):
    # chooses 1 random word out of a list of strings
    random_line = random.choice(a_list)
    print(random_line.strip().split())
    random_word = random.choice(random_line.strip().split())
    return random_word


def match_guess(word):
    # takes user input as word_guess
    # if guess == word, print "That's it!"
    # if any letters match between words, print "almost"
    # otherwise print nope

    while True:
        word_guess = input("Guess a word: ")
        if word_guess == word:
            print("That's it!")
            return
        elif word_guess in word:
            print("almost")
        elif any_char_in_word(word, word_guess):
            print("close")
        else:
            print("nope")


def any_char_in_word(word1, word2):
    # returns True if any characters in both words
    for char in word1:
        if char in word2:
            return True
    return False


def main(input_file):
    # reads in a file
    # chooses a random word from the file for user to guess
    lines = read_lines(input_file)
    random_word = get_random_word(lines)
    match_guess(random_word)


if __name__ == '__main__':
    main(sys.argv[1])
