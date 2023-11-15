import sys


def read_lines(filename):
    with open(filename) as file:
        return file.readlines()


def replace_digits(lines):
    # replaces digits with "#"

    new_list = []
    for line in lines:
        for char in line:
            if char.isdigit():
                line = line.replace(f"{char}", "#")
        new_list.append(line)
    return new_list


def write_lines(filename, content):
    with open(filename, 'w') as file:
        file.writelines(content)


def main(infile, outfile):
    lines = read_lines(infile)
    lines = replace_digits(lines)
    write_lines(outfile, lines)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
