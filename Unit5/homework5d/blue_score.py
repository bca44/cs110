from string import punctuation


def get_phrase():
    # gets input phrases until blank entered
    # returns list with each phrase string
    phrase_list = []
    while True:
        phrase = input("Phrase: ")
        if phrase == "":
            return phrase_list
        phrase_list.append(phrase)


def calculate_blue_score(phrase_list):
    """
    Calculate the 'blue score' for each phrase in the input list.
    Returns a list of tuples: ('phrase', score).
    """
    score_list = []
    for phrase in phrase_list:
        score = 0
        words = phrase.split()
        for word in words:
            if word.strip(punctuation).lower() in ["blue", "byu", "cougar", "cougars"]:
                score += 1
        score_list.append((phrase, score))
    return score_list


def group_dict(tuple_list):
    # makes a dict
    # keys are scores in list
    # values are each phrase that has given key
    score_phrase_dict = {}
    for phrase, score in tuple_list:
        if score not in score_phrase_dict:
            score_phrase_dict[score] = []
        score_phrase_dict[score].append(phrase)

    return score_phrase_dict


def dict_print(a_dict):
    for score in a_dict:
        print(f"{score}:")
        for phrase in a_dict[score]:
            print(f"{phrase}")
        print()


def main():
    # takes input phrases in a list of strings
    # for each string, calculates blue score
    # groups phrases by blue score in score_phrase_dict
    # prints dict
    phrases = get_phrase()
    # score_list is a list of tuples: (phrase, score)
    score_list = calculate_blue_score(phrases)
    score_groups = group_dict(score_list)
    dict_print(score_groups)


if __name__ == "__main__":
    main()
