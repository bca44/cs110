def get_places():
    # gets input from user until blank given
    # stores each input in 'places' list and returns list
    places = []

    while True:
        place = input("Enter a place: ")

        if place == "":
            break

        places.append(place)

    return places


def print_places(places):
    # prints "I have visited" message
    # prints each element of 'places' list passed to it, one at a time
    print("I have visited:")

    for place in places:
        print(f"- {place}")


def main():
    places = get_places()
    print_places(places)


if __name__ == '__main__':
    main()
