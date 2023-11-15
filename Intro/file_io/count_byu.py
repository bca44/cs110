import sys


def read_lines(filename):
    with open(filename) as file:
        return file.readlines()


def write_lines(content, filename):
    with open(filename, "w") as file:
        file.writelines(content)


def how_many(lines):
    # replaces each line's content with the count of B, Y, or U, lower or upper

    new_list, count = [], 0

    for line in lines:
        for char in line:
            if char.lower() in ["b", "y", "u"]:
                count += 1
        new_list.append(f"{count}\n")
        count = 0

    return new_list


def main(input_file, output_file):
    # reads line of input_file
    # replaces each line with a count of the characters [b, y, u, B, Y, U]
    # writes the results to the output_file

    lines = read_lines(input_file)
    lines = how_many(lines)
    write_lines(lines, output_file)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
