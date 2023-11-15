import sys


def read_lines(filename):
    with open(filename) as file:
        return file.readlines()


def write_lines(filename, content):
    with open(filename, "w") as file:
        file.writelines(content)


def profession_filter(a_list, wanted_profession):
    # filters all lines by profession value

    new_list = []

    for line in a_list:
        cust_id, gender, age, income, spending_score, profession, work_exp, family_size = line.split(",")
        if wanted_profession == profession:
            new_list.append(line)

    return new_list


def average_income(a_list):
    # finds average income of all lines in a_list

    total = 0

    for line in a_list:
        cust_id, gender, age, income, spending_score, profession, work_exp, family_size = line.split(",")
        total += int(income)

    # return the average
    return int(total / len(a_list))


def main(input_file, profession):
    # reads input_file - same CSV format and order
    # filters all lines with same 'profession' value
    # finds average income of those lines
    # prints "The average income of {profession} is {avg_income}"

    lines = read_lines(input_file)
    matched_lines = profession_filter(lines, profession)
    avg_income = average_income(matched_lines)
    print(f"The average income of {profession} is {avg_income}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
