import sys


def readlines(filename):
    with open(filename) as file:
        return file.readlines()


def writelines(filename, content):
    with open(filename, 'w') as file:
        file.writelines(content)



def change(line, grades):
    """
    Change line so that the student's grade is rounded up.
    Line has this form:

    name,grade\n

    You need to return:

    name,new_grade\n

    Notice the newline characters!
    """

    name, grade = line.strip().split(",")
    return f"{name},{grades[grade]}\n"


def change_grades(lines, grades):
    new_lines = []
    for line in lines:
        new_line = change(line, grades)
        new_lines.append(new_line)
    return new_lines


def main(infile, outfile):
    grades = { 'A' : 'A+',
               'A-' : 'A',
               'B+' : 'A-',
               'B' : 'B+',
               'B-' : 'B',
               'C+' : 'B-',
               'C' : 'C+',
               'C-' : 'C',
               'D+' : 'C-',
               'D' : 'D+',
               'D-' : 'D',
               'F' : 'D-'
             }
    lines = readlines(infile)
    lines = change_grades(lines, grades)
    writelines(outfile, lines)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
