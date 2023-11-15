def get_noun():
    noun = input("Noun: ")
    return noun


def get_adj():
    adj = input("Adjective: ")
    return adj


def get_number():
    number = input("Number: ")
    return number


def get_past_verb():
    verb = input("Past-Tense Verb: ")
    return verb


def get_game():
    game = input("Game: ")
    return game


def get_verb():
    verb = input("Verb: ")
    return verb


def assemble(noun1, adj1, adj2, noun2, number, adj3, past_verb, game, verb):
    print(f'Once upon a time a student at found themselves in a {noun1} class. The teacher was so {adj1} that the student started to daydream about a {noun2}. Then the student woke up and realized that they were still in class. The teacher was so {adj2} that they gave the student a {number} on the assignment. The student was so {adj3} that he {past_verb} the class and went home to play {game}. The moral of the story is that you should never {verb} in class.')

def mad_libs():
    print("Welcome to Mad Libs!")
    print("Please enter the following words:")
    noun1 = get_noun()
    adj1 = get_adj()
    adj2 = get_adj()
    noun2 = get_noun()
    number = get_number()
    adj3 = get_adj()
    past_verb = get_past_verb()
    game = get_game()
    verb = get_verb()
    assemble(noun1, adj1, adj2, noun2, number, adj3, past_verb, game, verb)

if __name__ == '__main__':
    mad_libs()
