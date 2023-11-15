def make_a_string(the_list):
    # makes a list of strings one string
    # capitalizes all strings
    # concatenates with '-' between

    a_string, i = '', 0

    for word in the_list:
        if i != len(the_list) - 1:
            a_string += word.upper() + '-'
        else:
            a_string += word.upper()
        i += 1
    return a_string


def main():
    the_list = ['yer', 'a', 'wizard', 'harry']
    print(make_a_string(the_list))
    the_list = ['what', 'does', 'the', 'fox', 'say']
    print(make_a_string(the_list))
    the_list = ['every', 'day', 'is', 'a', 'great', 'day', 'to', 'program']
    print(make_a_string(the_list))


if __name__ == '__main__':
    main()
