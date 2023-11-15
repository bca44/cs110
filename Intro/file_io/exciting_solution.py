import sys


def readlines(filename):
    with open(filename) as file:
        return file.readlines()
    

def writelines(filename, content):
    with open(filename, 'w') as file:
        file.writelines(content)
      
    
def add_bullets(lines):
    new_lines = []
    for line in lines:
        new_lines.append('⭐️ ' + fix_wording(line))
    return new_lines


def fix_wording(line):
    return line.replace('a boring', 'an exciting').replace('needs', 'has')

        
def main(infile, outfile):
    lines = readlines(infile)
    lines = add_bullets(lines)
    writelines(outfile, lines)
    
    
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
    
