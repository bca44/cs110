import sys


def read_lines(filename):
    with open(filename) as file:
        return file.readlines()


def add_line(lines):
    # adds "\n" after every line
    new_list = []
    for line in lines:
        line = line + "\n"
        new_list.append(line)

    return new_list


def write_lines(content, filename):
    with open(filename, "w") as file:
        file.writelines(content)


def main(input_file, output_file):
    # reads in input_file
    # adds "\n" after every line
    # writes result to output_file
    lines = read_lines(input_file)
    print(lines)
    lines = add_line(lines)
    write_lines(lines, output_file)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
