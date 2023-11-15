def get_strings():
    return input("First string: "), input("Second string: ")


def main():
    print("Let's concatenate strings!")
    while True:
        string1, string2 = get_strings()
        if string1 < string2:
            result = string1 + string2
            print(f"The result is {result}")
        else:
            print(f"Sorry, {string1} is greater than {string2}. I’m quitting.")


if __name__ == '__main__':
    main()
