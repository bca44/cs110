def get_tuple_list(text1, text2):
    # gets a list of tuples, ending with a blank line
    # uses given 'text' parameters as prompts for input
    # ends collection when element1 ""

    a_list = []

    while True:
        element1 = input(text1)
        if element1 == "":
            break
        element2 = input(text2)

        a_list.append((element1, element2))
    return a_list


def add_bonus(a_list, factor):
    # takes a list of tuples and a bonus factor
    # applies the bonus factor to the second element of each tuple and returns new list
    new_list = []
    for i in a_list:
        name, score = i
        score = float(score)
        score = round((score * (1 + factor)), 1)
        new_list.append((name, score))
    return new_list


def summary_scores(a_list, cutoff):
    # prints all tuples with scores higher than the cutoff

    high_scores = []
    for i in a_list:
        name, score = i
        if score >= cutoff:
            high_scores.append(i)
    print("High Scores:")
    [print(f"- {i[1]}: {i[0]}") for i in high_scores]


def main():
    print("Enter scores for each student.")
    print("Enter a blank student name to end.")
    score_list = get_tuple_list("Student: ", "Score: ")
    bonus = float(input("Bonus: "))
    cutoff = float(input("Cutoff: "))
    bonus_scores = add_bonus(score_list, bonus)
    summary_scores(bonus_scores, cutoff)


if __name__ == '__main__':
    main()
