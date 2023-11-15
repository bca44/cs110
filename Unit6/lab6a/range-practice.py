def print_list(items, therange):
    """
    <items> contains a list
    <therange> contains a range

    This function prints out *some* of the items in the list, using the
    supplied range.
    """
    print("Should print YES three times:")
    for i in therange:
        print(items[i])
    print()


def main():
    # Each of these have the wrong range given. The range should
    # cause print_list() to print YES three times.

    # Modify each range so that YES is printed 3 times in each case.
    print_list(['YES', 'YES', 'YES', 'NO', 'NO', 'NO'], range(0,3))
    print_list(['YES', 'NO', 'NO' ,'YES', 'NO', 'NO', 'YES'], range(0, 7, 3))
    print_list(['NO', 'YES', 'NO', 'YES', 'NO', 'YES'], range(-1, -6, -2))


if __name__ == '__main__':
    main()
