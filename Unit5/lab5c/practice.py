def do_counts():
    # initialize counts
    counts = {}
    while True:
        word = input("Word: ")
        if word == '':
            break

        if word not in counts:
            counts[word] = 0

        counts[word] += 1

    return counts


def main():
    counts = do_counts()
    print(counts)


if __name__ == '__main__':
    main()
