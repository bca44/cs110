import sys


def get_list(prompt, count):
    a_list = []

    while True:
        item = input(prompt + ": ")

        if item == "":
            break

        a_list.append(item)

    return a_list


def print_list(a_list):

    for item in a_list:

        print(f"- {item}")


def main(prompt, count):
    a_list = get_list(prompt, how_many)
    print_list(a_list)


if __name__ == "__main__":
    prompt = sys.argv[1]
    how_many = int(sys.argv[2])
    main(prompt, how_many)
