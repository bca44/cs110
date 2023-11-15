def get_name():
    # gets name from user and returns

    name = input("What is your name? ")
    return name


def get_pizza():
    # gets pizza type from user and returns

    pizza = input("What kind of pizza do you want? ")
    return pizza


def get_toppings():
    # gets toppings from user and returns

    toppings = input("What toppings do you want? ")
    return toppings


def print_summary(name, pizza, toppings):
    # prints order in fstring
    print(f'{name} wants a {pizza} pizza with {toppings}!')


def pizza_time():
    print("Welcome to Papa John's!")
    name = get_name()
    pizza = get_pizza()
    toppings = get_toppings()
    print_summary(name, pizza, toppings)


if __name__ == '__main__':
    pizza_time()
