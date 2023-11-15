import sys


def read_lines(filename):
    with open(filename) as file:
        return file.readlines()


def write_lines(content, filename):
    with open(filename, "w") as file:
        file.writelines(content)


def replace_vowels(lines):
    # replace vowels with "o"
    new_list = []

    for line in lines:
        for char in line:
            if char.lower() in ["a", "e", "i", "o", "u"]:
                line = line.replace(f"{char}", "o")
        new_list.append(line)

    return new_list


def main(input_file, output_file):
    # read in input file
    # replace all vowels with "o"
    # write new lines to output_file
    lines = read_lines(input_file)
    lines = replace_vowels(lines)
    write_lines(lines, output_file)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
