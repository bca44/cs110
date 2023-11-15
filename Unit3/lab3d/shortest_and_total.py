def shortest_word(words):
    # finds shortest word in provided list
    # initializes 'shortest' as first item, will replace it next is shortest

    shortest = words[0]

    for word in words:
        if len(word) < len(shortest):
            shortest = word
    return shortest


def total_lengths(words):
    # sums the length of all item in 'words'

    return sum(len(item) for item in words)


def main():
    words = ['the', 'elephant', 'ate', 'twenty', 'bananas', 'and', 'an', 'orange']
    shortest = shortest_word(words)
    total = total_lengths(words)
    print(f'The shortest word is: {shortest}')
    print(f'The total length of all the words is: {total}')


if __name__ == '__main__':
    main()
