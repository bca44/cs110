import sys


def main(a_list):

    product = 1

    for item in a_list:
        product *= int(item)

    print(float(product))


if __name__ == "__main__":
    main(sys.argv[1:5])
