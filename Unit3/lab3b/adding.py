def get_numbers():
    number1 = int(input("What's the first number? "))
    number2 = int(input("What's the second number? "))
    return number1, number2


def sigue():
    keep_going = input("Would you like to do more? ") not in ["no", "No"]
    return keep_going


def main():
    keep_going = True
    while keep_going:
        print("I can add numbers for you!")
        number1, number2 = get_numbers()
        result = number1 + number2
        print(f"The result is {result}.")
        keep_going = sigue()


if __name__ == '__main__':
    main()
