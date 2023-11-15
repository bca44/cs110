import sys


def main(a, b):
    print(f'{a} + {b} = {a + b}')
    

if __name__ == '__main__':
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    main(a, b)
    
