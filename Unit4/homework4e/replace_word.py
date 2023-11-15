import sys


def read_lines(filename):
    with open(filename) as file:
        return file.readlines()


def write_lines(filename, content):
    with open(filename, "w") as file:
        file.writelines(content)


def switch_words(a_list, old, new):
    # replaces each instance of old with new
    # at a word level, not substring level, btw

    new_list = []
    for line in a_list:
        for word in line.split():
            if word == old:
                line = line.replace(f"{word} ", f"{new} ")
        new_list.append(line)

    return new_list


def main(input_file, output_file, old_word, new_word):
    # reads input_file
    # replaces each instance of old_word with new_word
    # writes to output_file
    lines = read_lines(input_file)
    new_lines = switch_words(lines, old_word, new_word)
    write_lines(output_file, new_lines)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
