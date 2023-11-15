import sys


def readlines(filename):
    with open(filename) as file:
        return file.readlines()
    

def writelines(filename, content):
    with open(filename, 'w') as file:
        file.writelines(content)
    

def count_byu(line):
    total = 0
    for letter in line.lower():
        if letter in 'byu':
            total += 1
    return total


def process_lines(lines):
    new_lines = []
    for line in lines:
        new_lines.append(f'{count_byu(line)}\n')
    return new_lines

    
def main(inputfile, outputfile):
    lines = readlines(inputfile)
    lines = process_lines(lines)
    writelines(outputfile, lines)
    
    
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
    
