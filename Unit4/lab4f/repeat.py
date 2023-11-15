import random


def get_repeats(word):
    """
    Takes a word and returns a list of random numbers.
    There is one random number for each character in the word.
    """
    i, random_list = 0, []

    while i < len(word):
        random_list.append(random.randint(1, 10))
        i += 1

    return random_list


def do_repeats(word, repeats):
    """
    Takes a word and a list of numbers.
    Returns a new word that repeats each character in the word
    based on its corresponding number in the list.

    So do_repeats('wow', [2, 4, 3]) will return 'wwoooowww'
    """
    new_word = ""
    for char, rand_int in zip(word, repeats):
        new_word = new_word + (char * rand_int)

    return new_word


def main():
    word = input("Enter a word: ")
    repeats = get_repeats(word)
    new_word = do_repeats(word, repeats)
    print(new_word)


if __name__ == '__main__':
    main()
