import sys


def encode(codex, message):
    """
    Returns the encoded message using the codex dictionary.
    Preserves casing of characters and spacing between words.
    Characters not listed in the codex are not modified.
    """

    coded_message = []

    for word in message.split():
        coded_word = []

        for char in word:
            if char.islower() and char in codex:
                char = codex[char]

            elif char.isupper() and char.lower() in codex:
                char = codex[char.lower()].upper()

            coded_word.append(char)

        coded_message.append("".join(coded_word))

    return " ".join(coded_message)


def main(message, codex):
    encoded = encode(codex, message)
    print(encoded)


if __name__ == '__main__':
    simple_codex = {
        'a': 'd',
        'b': 'e',
        'c': 'z',
        'd': 'h',
        'e': 'g',
        'f': 's',
        'g': 'n',
        'h': 'r',
        'i': 'a',
        'j': 'b',
        'k': 'k',
        'l': 'j',
        'm': 'c',
        'n': 'u',
        'o': 'y',
        'p': 't',
        'q': 'q',
        'r': 'x',
        's': 'w',
        't': 'v',
        'u': 'p',
        'v': 'f',
        'w': 'i',
        'x': 'l',
        'y': 'm',
        'z': 'o'
    }
    main(sys.argv[1], simple_codex)
