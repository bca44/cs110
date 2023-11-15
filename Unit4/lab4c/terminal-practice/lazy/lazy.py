import sys


def lazy(length, unit):
    print("You're feeling lazy?")
    print(f"Ok, take {number} {unit}(s) off and be kind to yourself.")


if __name__ == '__main__':
    if len(sys.argv) <= 2:
        print("This program takes two arguments:")
        print("- a number")
        print("- a unit of time (day, week, month, year")
        exit()


    number = int(sys.argv[1])
    unit = sys.argv[2]
    lazy(number, unit)
