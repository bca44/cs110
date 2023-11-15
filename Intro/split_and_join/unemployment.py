import sys


def read_lines(filename):
    with open(filename) as file:
        return file.readlines()


def max_unemployment(lines, state):
    # returns line with highest unemployment rate for given state

    highest_rate, highest_line = 0, []

    for line in lines:
        split_line = line.split()

        # filters results, allows lines with matching "state" values
        if state.upper() == split_line[0].upper():

            # finds line with highest "unemployment %" value
            if float(split_line[3]) > highest_rate:
                highest_line = line

    return highest_line


def print_line(highest_line):
    # prints summary of highest line in sentence format
    state, year, month, percent = highest_line.split()
    print(f"{state} had {percent} percent unemployment in {year} month {month}")


def main(input_file, state):
    # reads in input_file
    lines = read_lines(input_file)
    # finds line with highest unemployment rate for that state
    highest_line = max_unemployment(lines, state)
    # prints highest_line results
    print_line(highest_line)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
