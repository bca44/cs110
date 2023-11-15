def give_compliment():
    print("You handsome devil you!")


def give_advice():
    print("Don't forget to brush those pearly whites.")


def main():
    while True:
        option = input("""
        What would you like to do?
            1) Receive compliment
            2) Receive advice
            3) Quit
        Option: """)
        if option == "1":
            give_compliment()
        elif option == "2":
            give_advice()
        elif option == "3":
            break


if __name__ == '__main__':
    main()
