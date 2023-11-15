def ratings_for_flavor(ratings, requested_flavor):
    # sorts a list of tuples by common first elements, matching the second parameter given

    new_list = []

    for i in ratings:
        if i[0] == requested_flavor:
            new_list.append(i)
    return new_list


def get_average(ratings):
    # takes the average of the second elements of a list of tuples

    sum = 0

    for i in ratings:
        sum += i[1]

    return round(sum / len(ratings), 1)


def print_info(ratings, flavor):
    # prints the name and average rating of a flavor

    average = get_average(ratings)
    print(f"The average rating for {flavor} is {average}.")


def main():
    ratings = [('chocolate', 10), ('banana nut', 8.5), ('vanilla', 6),
              ('chocolate', 9), ('banana nut', 9.3), ('vanilla', 7.5),
              ('chocolate', 8), ('banana nut', 10), ('vanilla', 4.1),
              ('chocolate', 10), ('banana nut', 10), ('vanilla', 10),
              ('chocolate', 9.3), ('banana nut', 7.5), ('vanilla', 8)
              ]
    flavors = ['chocolate', 'banana nut', 'vanilla']
    for flavor in flavors:
        new_ratings = ratings_for_flavor(ratings, flavor)
        print_info(new_ratings, flavor)


if __name__ == '__main__':
    main()
