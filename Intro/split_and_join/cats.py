def has_cat(text):
    words = text.split()
    return 'cat' in words


if __name__ == '__main__':
    phrases = [
        'I have a dog.',
        'My cat eats bugs.',
        'Can you concatenate two strings?'
    ]
    for phrase in phrases:
        print(phrase)
        print(f'has_cat: {has_cat(phrase)}')
        print(f'"cat" in: {"cat" in phrase}')
        print()
        
