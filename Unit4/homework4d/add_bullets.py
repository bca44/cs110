import sys


def read_lines(filename):
    with open(filename) as file:
        return file.readlines()


def write_lines(content, filename):
    with open(filename, "w") as file:
        file.writelines(content)


def add_bullet(lines, bullet):
    # adds bullet before each line
    new_list = []

    for line in lines:
        new_list.append(f"{bullet} " + line)
    return new_list


def main(input_file, output_file, bullet_string):
    # reads in input_file
    # adds "{bullet_string} " before each line
    # writes adjusted lines to output_file
    lines = read_lines(input_file)
    lines = add_bullet(lines, bullet_string)
    write_lines(lines, output_file)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
