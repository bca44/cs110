import sys


def read_lines(filename):
    with open(filename) as file:
        return file.readlines()


def write_lines(content, filename):
    with open(filename, "w") as file:
        file.writelines(content)


def numbers_only(lines):
    # allows lines that don't contain "NaN"
    new_list = []
    for line in lines:
        if "NaN" not in line:
            new_list.append(line)
    return new_list


def main(input_file, output_file):
    # reads in input_file
    # filters lines, allows lines that don't contain "NaN"
    # writes new lines to output_file
    lines = read_lines(input_file)
    lines = numbers_only(lines)
    write_lines(lines, output_file)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
