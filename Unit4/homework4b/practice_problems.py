def for_reals(text):
    """
    Replace all '%' with ' percent' and all '!' with ' (for reals).'
    Notice the spaces!    ^                           ^
    Return the new text.
    """

    text = text.replace('%', ' percent')
    text = text.replace('!', ' (for reals).')

    return text


def doubles(text):
    """
    Replace all 'oo' with 'oooooo' and all 'ee' with 'eeeeee'.
    Return the new text.
    """

    text = text.replace('oo', 'oooooo')
    text = text.replace('ee', 'eeeeee')

    return text


def only_o(text):
    """
    Replace all vowels (aeiou) with 'o'
    Preserve the casing of each letter.
    Return the new text.
    """

    for char in text:

        if char in ['a', 'e', 'i', 'u']:
            text = text.replace(f'{char}', 'o')

        elif char in ['A', 'E', 'I', 'U']:
            text = text.replace(f'{char}', 'O')

    return text


def upper_vowels(text):
    """
    Make all vowels uppercase.
    Return the new text.
    """

    for char in text:

        if char in ["a", "e", "i", "o", "u"]:
            text = text.replace(char, char.upper())

    return text

