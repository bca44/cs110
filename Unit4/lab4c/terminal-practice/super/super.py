import sys


def main(superlative):
    print(f"Have a {superlative} day!")


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("This program takes one argument, a superlative.")
        print("For example: 'stupendous' or 'fantastic'")
        exit()

    superlative = sys.argv[1]
    main(superlative)
