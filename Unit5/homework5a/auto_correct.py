import sys


def read_lines(filename):
    """Read lines from a file and return a list of lines."""
    with open(filename) as file:
        return file.readlines()


def write_lines(filename, content):
    """Write a list of lines to a file."""
    with open(filename, "w") as file:
        file.writelines(content)


def autocorrector(lines, corrections_dict):
    """
    Take a list of lines and a corrections dictionary.
    Correct each line using the dictionary and return a new list of corrected lines.
    """
    corrected_lines = []

    for line in lines:
        corrected_line = correct_line(line, corrections_dict)
        corrected_lines.append(corrected_line + "\n")

    return corrected_lines


def correct_line(line, corrections_dict):
    """
    Take a line and a corrections dictionary.
    Substitute dictionary keys with their values and return the corrected line.
    """
    corrected_words = []

    for word in line.split():
        if word in corrections_dict:
            word = corrections_dict[word]
        corrected_words.append(word)

    return " ".join(corrected_words)


def main(input_file, output_file, corrections_dict):
    """
    Read lines from the input file, autocorrect them using the corrections dictionary,
    and write the corrected lines to the output file.
    """
    lines = read_lines(input_file)
    corrected_lines = autocorrector(lines, corrections_dict)
    write_lines(output_file, corrected_lines)


if __name__ == "__main__":
    corrections = {
        'teh': 'the',
        'adn': 'and',
        'thye': 'they',
        'yuo': 'you',
        'i': 'I'
    }
    main(sys.argv[1], sys.argv[2], corrections)
