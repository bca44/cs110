import sys


def readlines(filename):
    with open(filename) as file:
        return file.readlines()
    

def writelines(filename, content):
    with open(filename, 'w') as file:
        file.writelines(content)
        
        
def make_upper(lines):
    new_lines = []
    for line in lines:
        new_lines.append(line.upper())
    return new_lines

        
def main(input_file, output_file):
    lines = readlines(input_file)
    lines = make_upper(lines)
    writelines(output_file, lines)
    
    
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
    
