import random

def ummify(text):
    """
    Randomly inject 'umm' into the given text at a frequence of 20%
    """
    words = text.split(' ')
    result = []
    for word in words:
        if random.random() < 0.2:
            result.append('umm')
        result.append(word)
    return ' '.join(result)


if __name__ == '__main__':
    speech = ["Four score and seven years ago our fathers brought forth, on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.",
    "Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war.",
    "We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this."]

    for line in speech:
        print(ummify(line))
