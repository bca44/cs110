import sys


def main(sys_arg):
    while True:

        guess = input("Guess: ")

        if guess == sys_arg:
            print("You got it!")
            break
        elif sys_arg in guess:
            print("It's in there...")
        else:
            print("Nope.")


if __name__ == "__main__":
    main(sys.argv[1])
