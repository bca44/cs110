import sys


def main(input_file, output_file):
    # reads in input_file
    # changes "a boring" to "an exciting"
    # puts "* " at the start of each line
    # writes new lines to output_file

    lines = read_lines(input_file)
    lines = add_star(lines)
    write_lines(lines, output_file)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])


def read_lines(filename):
    with open(filename) as file:
        return file.readlines()


def add_star(lines):
    # adds "* " to start of each line
    new_lines = []
    for line in lines:
        new_lines.append("⭐️ " + change_words(line))
    return new_lines


def change_words(line):
    # changes "a boring " to "an exciting " and "needs " to "has "
    return line.replace("a boring ", "an exciting ").replace("needs ", "has ")


def write_lines(content, filename):
    with open(filename, "w") as file:
        file.writelines(content)
