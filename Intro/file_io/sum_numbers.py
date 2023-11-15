import sys


def readlines(filename):
    with open(filename) as file:
        return file.readlines()
    

def writelines(filename, content):
    with open(filename, 'w') as file:
        file.writelines(content)
        
        
def as_floats(line):
    """Turn '0.7 0.8' into [0.7, 0.8]"""
    numbers = []
    for string in line.split():
        numbers.append(float(string))
    return numbers


def sum_number_strings(line):
    """Turn '0.7 0.8' into 1.5"""
    numbers = as_floats(line)
    return sum(numbers)


def sum_each_line(lines):
    """Turn ['0.7 0.8', '0.1 0.3 2.0', ...] into [1.5, 2.4, ...]"""
    totals = []
    for line in lines:
        totals.append(sum_number_strings(line))
    return totals


def format_totals(totals):
    """Turn [1.5, 2.4, ...] into ['1.5\n', '2.4\n', ...]"""
    lines = []
    for total in totals:
        lines.append(f'{total}\n')
    return lines

    
def main(input_file, output_file):
    lines = readlines(input_files)
    totals = sum_each_line(lines)
    lines = format_totals(totals)
    writelines(lines)
    
    
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
    
