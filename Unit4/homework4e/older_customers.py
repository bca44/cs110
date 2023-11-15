import sys


def read_lines(filename):
    with open(filename) as file:
        return file.readlines()


def write_lines(filename, content):
    with open(filename, "w") as file:
        file.writelines(content)


def get_older(a_list, min_age):
    # keeps first string as header
    # filters rest by min_age

    old_list = []

    for line in a_list:
        cust_id, gender, age, income, spending_score, profession, work_exp, family_size = line.split(",")
        if int(age) > min_age:
            old_list.append(line)

    return old_list


def add_header(header_list, content_list):
    # adds header_list[0] to rest of content_list

    new_list = [header_list[0]]

    for line in content_list:
        new_list.append(line)

    return new_list


def main(input_file, output_file, min_age):
    # reads input_file
    # input_file fields are: cust id, gender, age, income, spending score, profession, work experience, family size
    # writes to output each line with age value > min_age
    lines = read_lines(input_file)
    old_lines = get_older(lines[1:], min_age)
    old_lines = add_header(lines, old_lines)
    write_lines(output_file, old_lines)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]))
