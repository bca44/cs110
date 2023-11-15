def get_name():
    return input("What is your name? ")


def get_sandwich():
    return input("What kind of sandwich do you want? ")


def get_additions():
    return input("What do you want on it? ")


def print_summary(name, sandwich_type, adds):
    print(f'{name} wants a {sandwich_type} sandwich with {adds}!')


def main():
    print("Welcome to Wendy's!")
    name = get_name()
    sandwich_type = get_sandwich()
    adds = get_additions()
    print_summary(name, sandwich_type, adds)

if __name__ == '__main__':
    main()
