import sys


def read_lines(filename):
    with open(filename) as file:
        return file.readlines()


def write_lines(filename, content):
    with open(filename, 'w') as file:
        file.writelines(content)


def double_quantity(line):
    #
    # for each word in each line
    for word in line.split():
        if word.isdigit():
            line = line.replace(f"{word}", f"{int(word) * 2}")

    return line


def double_quantities(lines):
    # doubles each numeric element of the lines list
    new_list = []

    # each line of file input
    for line in lines:
        line = double_quantity(line)
        new_list.append(line)

    return new_list


def main(input_file, output_file):
    # finds and doubles any numeric word
    # writes all lines to output_file
    lines = read_lines(input_file)
    doubled_lines = double_quantities(lines)
    write_lines(output_file, doubled_lines)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
