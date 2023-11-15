def count_whitespace(string: str) -> int:
    # counts the number of whitespaces in given string

    total = 0
    for char in string:
        if char.isspace():
            total += 1

    return total


def keep_big_words(words: list[str]) -> list[str]:
    # returns a list of strings with more than 3 uppercase letters

    big_list = []

    for string in words:

        big_count = 0

        for char in string:

            if char.isupper():
                big_count += 1

        if big_count > 3:
            big_list.append(string)

    return big_list


def most_punctuation(words: list[str]) -> str:
    # returns the word with the most punctuation, i.e., chars not space, al, or num

    biggest, biggest_count = "", 0

    for string in words:

        current_count = 0

        for char in string:

            if not char.isspace() and not char.isalnum():
                current_count += 1

        if current_count > biggest_count:
            biggest, biggest_count = string, current_count

    return biggest


def remove_punctuation(string: str) -> str:
    # removes all punctuation from the string

    new_string = ""

    for char in string:

        if char.isspace() or char.isalnum():
            new_string += char

    return new_string


def replace_digits_with_asterisks(string: str) -> str:
    # replaces digits in the string with "*"

    new_string = ""

    for char in string:

        if char.isnumeric():
            char = "*"

        new_string += char

    return new_string
