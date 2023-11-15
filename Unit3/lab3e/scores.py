def find_highest_score(scores):
    # accepts as input a list of tuples. compares the 2nd element to find which is the highest
    # returns the highest tuple

    highest = scores[0]

    for i in scores:
        if i[2] > highest[2]:
            highest = i

    return highest


def main():
    scores = [('Johns', 'Hayden', 72), ('Rodriguez', 'Emily', 94), ('Young', 'Henry', 91), ('Bean', 'Alma', 95), ('Peterson', 'Roger', 83)]
    last, first, score = find_highest_score(scores)
    print(f"Highest score: {first} {last}, {score}")


if __name__ == '__main__':
    main()
