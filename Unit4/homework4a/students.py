def get_tuple_list(text1, text2, text3):
    # gets a list of tuples, ending with a blank line
    # uses given 'text' parameters as prompts for input
    # ends collection when element1 ""

    a_list = []

    while True:
        print("Enter a student.")
        element1 = input(text1)
        if element1 == "":
            break
        element2 = input(text2)
        element3 = input(text3)

        a_list.append((element1, element2, element3))
    return a_list


def school_sort(a_list):
    #

    byu_list, other_list = [], []

    for name, hometown, school in a_list:
        if school == "BYU":
            name = name.upper()
            byu_list.append((name, hometown, school))
        else:
            other_list.append((name, hometown, school))

    return byu_list, other_list


def summary(a_list, title):
    #
    print(f"{title} Students:")
    for name, hometown, school in a_list:
        print(f"- {name}")


def main():
    student_list = get_tuple_list("Name: ", "Hometown: ", "School: ")
    byu_list, other_list = school_sort(student_list)
    summary(byu_list, "BYU")
    summary(other_list, "Other")


if __name__ == "__main__":
    main()
