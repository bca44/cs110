def get_player_info(jerseys):
    name = input("Player name: ")
    if name == '':
        return None
    while True:
        number = input("Jersey number: ")
        if number not in jerseys:
            return name, number
        print("That number is already taken.")


def assign_jerseys():
    players = []
    jerseys = []

    while True:

        player = get_player_info(jerseys)
        if player is None:
            break
        players.append(player)

        name, jersey = player
        jerseys.append(jersey)

    return players


def print_assignments(players):
    """
    Prints a list of players using this output:
    number: name
    """

    for name, number in players:
        print(f"{number}: {name}")
        

def main():
    players = assign_jerseys()
    print_assignments(players)


if __name__ == '__main__':
    main()
