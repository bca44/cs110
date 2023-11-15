import sys


def read_lines(filename):
    with open(filename) as file:
        return file.readlines()


def write_lines(filename, content):
    with open(filename, "w") as file:
        file.writelines(content)


def find_sum(a_list):
    # adds up each int found in a list of strings

    total = 0

    for line in a_list:
        for word in line.split():
            if word.isdigit():
                total += int(word)

    return total


def main(input_file):
    # reads input file, each line having various int
    # sums all numbers in file
    # prints, "The total is {sum}"
    lines = read_lines(input_file)
    total = find_sum(lines)
    print(f"The total is {total}")


if __name__ == "__main__":
    main(sys.argv[1])
