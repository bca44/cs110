import sys


def add_emojis(text, emojis):
    """Replace words in `emojis` with their corresponding symbols."""

    new_words = []
    for word in text.split():
        if word in emojis:
            word = emojis[word]
        new_words.append(word)

    return " ".join(new_words)


if __name__ == '__main__':
    emojis = {
        'dog': '🐶',
        'puppy': '🐶',
        'dogs': '🐶🐶',
        'cat': '🐱',
        'tree': '🌳',
        'bird': '🐦'
    }
    print(add_emojis(sys.argv[1], emojis))
