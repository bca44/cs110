def not_full(slots):
    """
    <slots> -- a list of slots -- either "empty" or a Pokemon
    Returns true if any slot is equal to "empty"
    """
    if "empty" in slots:
        return True
    return False


def print_choices(available):
    """
    <available> -- a list of Pokemon

    Prints all of the available Pokemon
    """
    print("Available Pokemon:")
    for i in range(len(available)):
        print(f"({i}) {available[i]} ")
    print()


def get_choice(available):
    """
    <available> -- a list of Pokemon

    Gets a choice of Pokemon (an integer entered with input()).
    Returns the Pokemon in this place on the list.
    """
    choice = int(input("Choice: "))
    return available[choice]


def add_pokemon(slots, pokemon):
    """
    <slots> -- a list of slots -- either "empty" or a Pokemon
    <pokemon> -- the name of a Pokemon

    Modifies <slots> so that <pokemon> is in the first slot
    that is equal to "empty".
    """
    for i in range(len(slots)):
        if slots[i] == "empty":
            slots[i] = pokemon
            return


def print_pokemon(slots):
    """
    <slots> -- a list of slots -- either "empty" or a Pokemon

    Prints the Pokemon in all the slots
    """
    print("Your Pokemon:")
    for i in range(len(slots)):
        print(f"({i}) {slots[i]}")


def main():
    # the list of available Pokemon
    available = ['bulbasaur', 'charmander', 'squirtle', 'pikachu', 'jigglypuff',
               'meowth', 'machop', 'drowzee', 'staryu', 'magikarp', 'dragonite']

    print("Choose your Pokemon!")
    # three slots, all empty
    slots = ['empty' ,'empty', 'empty']
    # keep going as long as the slots are not full
    while not_full(slots):
        # print the Pokemon available to be drafted
        print_choices(available)
        # draft a Pokemon
        pokemon = get_choice(available)
        # put that Pokemon in the next available slot
        add_pokemon(slots, pokemon)

    # print the drafted Pokemon
    print_pokemon(slots)


if __name__ == '__main__':
    main()
