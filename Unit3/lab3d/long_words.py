def long_words(words):
    long_words = [i for i in words if len(i) > 5]
    return long_words


def print_words(words):
    [print(f"- {i}") for i in words]


def main():
    words = ['completely', 'fun', 'program', 'to', 'write', 'hahaha']
    long = long_words(words)
    print_words(long)


if __name__ == '__main__':
    main()
