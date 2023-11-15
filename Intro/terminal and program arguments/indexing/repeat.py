import sys


def main(phrase, how_many):
    print(phrase * how_many)
    

if __name__ == '__main__':
    phrase = sys.argv[1]
    how_many = int(sys.argv[2])
    main(phrase, how_many)
    
