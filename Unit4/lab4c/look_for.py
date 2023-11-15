import sys


def main(substring):

    while True:

        word_phrase = input("Enter a word or phrase: ")
        if word_phrase == "":
            break
        elif substring in word_phrase:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    look_for = sys.argv[1]
    main(look_for)
