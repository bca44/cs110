import sys


def readlines(filename):
    with open(filename) as file:
        return file.readlines()
    
    
if __name__ == '__main__':
    lines = readlines(sys.argv[1])
    print(lines)
    
