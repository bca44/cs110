def add():
    # takes two input numbers, prints the sum

    number1, number2 = int(input("Number 1: ")), int(input("Number 2: "))
    print(number1 + number2)

def subtract():
    # takes two input numbers, prints the difference

    number1, number2 = int(input("Number 1: ")), int(input("Number 2: "))
    print(number1 - number2)


def calculator():

    while True:

        response = input("""
What would you like to do?
 1) Add
 2) Subtract
 3) Quit
Option: """)

        if response == "3":
            break

        elif response == "1":
            add()

        elif response == "2":
            subtract()
        else:
            print(f"Unrecognized response: {response}")


if __name__ == '__main__':
    calculator()
