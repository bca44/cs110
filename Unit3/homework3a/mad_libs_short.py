def get_noun():
    noun = input("Noun: ")
    return noun


def get_adj():
    adj = input("Adjective: ")
    return adj


def get_character():
    character = input("Character: ")
    return character


def get_animal():
    animal = input("Animal (Plural): ")
    return animal


def assemble(noun1, adj, noun2, character, animal):
    print(f"{noun1} sat on a {noun2}. {noun1} had a {adj} fall. All {character}'s {animal} and all the {character}'s men couldn't put {noun1} together again.")


def mad_libs_short():
    print("Welcome to Mad Libs!")
    print("Please enter the following words:")

    noun1 = get_noun()
    adj = get_adj()
    noun2 = get_noun()
    character = get_character()
    animal = get_animal()

    assemble(noun1, adj, noun2, character, animal)


if __name__ == '__main__':
    mad_libs_short()
