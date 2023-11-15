import random

def shuffle(string):
    """
    Use random.sample to get the letters in the string in a random order.
    Then join the letters together with the empty string.
    """
    shuffled_letters = random.sample(string, len(string))
    return ''.join(shuffled_letters)


if __name__ == '__main__':
    shuffled = shuffle('Washington')
    print(shuffled)
