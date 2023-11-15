import sys


def add(num1, num2):
    print(num1 + num2)


def sub(num1, num2):
    print(num1 - num2)


if __name__ == '__main__':
    operation = sys.argv[1]
    arg1 = int(sys.argv[2])
    arg2 = int(sys.argv[3])

    if operation == "add":
        add(arg1, arg2)
    elif operation == "sub":
        sub(arg1, arg2)
    else:
        print("Unsupported operation. Did you mean 'add' or 'sub'?")
