import random
import sys


def read_lines(filename):
    with open(filename) as file:
        return file.readlines()


def random_word(a_list):
    # picks one random word from given list of words
    return random.choice(a_list).strip()


def match_spaces(guess, key_word):
    # matches guess to key_word
    # print off 'feedback' [!, ?, *] according to key

    print_this = []

    for char1, char2 in zip(guess, key_word):
        if char1 == char2:
            print_this.append("!")
        elif char1 in key_word:
            print_this.append("?")
        else:
            print_this.append("*")

    print("".join(print_this))


def wordle_me_this(key_word, guess_max):
    """
    prompts for player input
    matches player's guess to given key_word
    key: "!" (exactly right), "?" (right, wrong place), "*" (not in word)
    """

    attempt = 1
    while attempt <= guess_max:
        guess = input(f"Guess # {attempt}: \n")
        attempt += 1
        if guess == key_word:
            match_spaces(guess, key_word)
            print("Way to go!")
            return
        else:
            match_spaces(guess, key_word)
    print(f"Maybe next time. The answer is {key_word}.")


def main(word_bank, guess_max):
    all_words = read_lines(word_bank)
    chosen_word = random_word(all_words)
    wordle_me_this(chosen_word, guess_max)


if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
