import sys


def readlines(filename):
    with open(filename) as file:
        return file.readlines()
    

def as_ints(str_numbers):
    nums = []
    for str_num in str_numbers:
        nums.append(int(str_num))
    return nums


def main(filename):
    lines = readlines(filename)
    numbers = as_ints(lines)
    total = sum(numbers)
    print(f'The total in {filename} is {total}')
    
    
if __name__ == '__main__':
    main(sys.argv[1])
    
