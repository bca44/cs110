import sys


def read_lines(filename):
    with open(filename) as file:
        return file.readlines()


def make_dict(a_list):
    # makes a dictionary out of a list of comma-separated key-value tuples
    a_dict = {}

    for element in a_list:
        key, value = element.split(",")
        a_dict[key] = value

    return a_dict


def find_total(quan_dict, price_dict):
    # finds the total of each item wanted
    total = 0.0

    for item in quan_dict:
        quantity = float(quan_dict[item])
        price = float(price_dict[item])
        total += quantity * price

    return round(total, 2)


def main(item_file, price_file):
    # takes an item file and a price file
    # creates an item_quan_dict and an item_price_dict
    # uses the two to find cart total

    item_quan_list = read_lines(item_file)
    item_price_list = read_lines(price_file)

    item_quan_dict = make_dict(item_quan_list)
    item_price_dict = make_dict(item_price_list)

    cart_total = find_total(item_quan_dict, item_price_dict)
    print(f"The total is ${cart_total}")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
