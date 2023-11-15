import random


def random_asterisks(text, frequency):
    """
    At the given frequency, randomly replace words with a string of asterisks
    The asterisks should be the same length as the word being replaced.
    """

    new_text = []
    for word in text.split():
        probability = random.random()
        if probability < frequency:
            word = "*"

        new_text.append(word)

    new_text = " ".join(new_text)
    print(new_text)
    return(new_text)


if __name__ == '__main__':
    random_asterisks("my dog has fleas", 0.5)
