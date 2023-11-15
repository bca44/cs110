import sys


def readlines(filename):
    with open(filename) as file:
        return file.readlines()
    

def writelines(filename, content):
    with open(filename, 'w') as file:
        file.writelines(content)
        
        
def cat_to_cougar(line):
    words = line.split()
    new_words = []
    for word in words:
        if word == 'cat':
            word = 'cougar'
        new_words.append(word)
    return ' '.join(new_words) + '\n'  # what happens when you forget the '\n'?


def cats_are_cougars(lines):
    new_lines = []
    for line in lines:
        new_lines.append(cat_to_cougar(line))
    return new_lines


def main(input_file, output_file):
    lines = readlines(input_file)
    lines = cats_are_cougars(lines)
    writelines(output_file, lines)
    
    
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
    
