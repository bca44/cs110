def do_subs(line):
    """
    Put cat emojis around words with 'cat' in them.
    Put dog emojis around words with 'dog' in them
    - create an empty list
    - split the line into words
    - go through all the words
    - if the word has 'cat' in it, put '🐈' at the front and end
    - if the word has 'dog' in it, put '🐕' at the front and end
    - append all the words to the new list
    - join the new list using space as the join character
    """
    new_list = []

    for word in line.split():
        if "cat" in word:
            line = line.replace(f"{word}", f"🐈 {word} 🐈")
        elif "dog" in word:
            line = line.replace(f"{word}", f"🐕 {word} 🐕")
    new_list.append(line)

    return new_list


def main():
    """
    - allow a person to enter lines
    - stop when you get to a blank line
    - call the do_subs() function to change the line
    - print the changed line
    """
    while True:
        line = input("> ")
        if line == '':
            return
        line = do_subs(line)
        print(line)


if __name__ == '__main__':
    main()
