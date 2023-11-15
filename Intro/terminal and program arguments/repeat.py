import sys


def repeat(text, number):
    print(text * number)
    

if __name__ == '__main__':
    text = sys.argv[1]
    number = int(sys.argv[2])
    repeat(text, number)