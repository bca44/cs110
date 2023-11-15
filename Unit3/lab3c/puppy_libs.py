def get_ing():
    # collects user input until "" entered
    # stores them in 'verbs' list and returns it
    verbs = []

    while True:

        verb = input('Enter a verb ending in "ing": ')

        if verb == "":
            break

        verbs.append(verb)
    return verbs


def print_ing(verbs):
    # prints each element of list 'verbs'
    # ends with 'nap' statement
    for verb in verbs:
        print(f"The puppy is {verb}!")

    print("The puppy is taking a nap.")


def main():
    verbs = get_ing()
    print_ing(verbs)


if __name__ == '__main__':
    main()
