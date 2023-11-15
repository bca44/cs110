def cats_to_cougars(line):
    words = line.split()
    new_words = []
    for word in words:
        if word == 'cat':
            word = 'cougar'
        new_words.append(word)
    return ' '.join(new_words)


def main():
    lines = ["BYU's mascot is cool, like a cat or something.",
             "Just like a cat can, he can catch stuff."]
    for line in lines:
        print(cats_to_cougars(line))


if __name__ == '__main__':
    main()
    
