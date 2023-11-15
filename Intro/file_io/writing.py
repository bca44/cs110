import sys


def writelines(filename, content):
    with open(filename, 'w') as file:
        file.writelines(content)
        
        
if __name__ == '__main__':
    content = ['one\n', 'two\n', 'three\n', 'four\n']
    writelines(sys.argv[1], content)
    
