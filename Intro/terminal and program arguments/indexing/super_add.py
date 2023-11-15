import sys


def main(a, b):
    print(f'{a} + {b} = {a + b}')
    

if __name__ == '__main__':
    style = sys.argv[1]
    if style == 'str':
        a = sys.argv[2]
        b = sys.argv[3]
        
    elif style == 'num':
        a = float(sys.argv[2])
        b = float(sys.argv[3])
        
    else:
        print(f'Unrecognized style: {style}')
        
    main(a,b)
    
