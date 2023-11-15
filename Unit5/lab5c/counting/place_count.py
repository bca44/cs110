def get_places():
    # create an empty dictionary
    places = {}
    while True:
        # get a place
        place = input('State or Country: ')
        # break if we are done
        if not place:
            break
        # if this place is not in the dictionary yet
        # then initialize this place to zero
        if place not in places:
            places[place] = 0
        # increment this place by one
        # this doesn't cause an error because we were sure
        # to initialize it to zero above
        places[place] += 1

    # return the dictionary
    return places

def main():
    places = get_places()
    print(places)


if __name__ == '__main__':
    main()
