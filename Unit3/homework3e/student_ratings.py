def get_tuple_list(text1, text2):
    # gets a list of tuples, ending with a blank line
    # uses given 'text' parameters as prompts for input

    a_list = []

    while True:
        element1 = input(text1)
        if element1 == "":
            break
        element2 = input(text2)

        a_list.append((element1, element2))
    return a_list


def get_average(ratings):
    # takes the average of the second elements of a list of tuples

    total = 0

    for i in ratings:
        total += float(i[0])

    print(f"Average rating: {round(total / len(ratings), 1)}")


def print_comments(ratings):

    print("Comments:")

    for i in ratings:
        print(f"- {i[1]}")


def main():
    print("""Enter ratings for this class.
Each rating includes a score and a comment.
Use a blank score to end.""")
    ratings = get_tuple_list("Score: ", "Comment: ")
    get_average(ratings)
    print_comments(ratings)


if __name__ == '__main__':
    main()
