import sys


def read_lines(filename):
    with open(filename) as file:
        return file.readlines()


def write_lines(content, filename):
    with open(filename, "w") as file:
        file.writelines(content)


def redact(lines, pattern):
    # replaces all substrings matching pattern with "****"
    new_list = []

    for line in lines:
        if pattern in line:
            line = line.replace(f"{pattern}", "****")
        new_list.append(line)

    return new_list


def main(input_file, output_file, string_pattern):
    # read in input file
    # replaces string_pattern with "****"
    # writes new lines to output_file
    lines = read_lines(input_file)
    lines = redact(lines, string_pattern)
    write_lines(lines, output_file)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
