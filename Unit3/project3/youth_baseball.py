def get_tuple_list(prompt_name, prompt_age):
    """
    Collects a list of player names and ages, ending with a blank input.

    Args:
        prompt_name (str): The prompt to enter a player's name.
        prompt_age (str): The prompt to enter a player's age (integer).

    Returns:
        list: A list of tuples containing player names and ages.
    """
    player_list = []

    while True:
        name = input(prompt_name)
        if name == "":
            break
        age = int(input(prompt_age))
        player_list.append((name, age))

    return player_list


def sort_by_age(player_list):
    """
    Sorts players into two lists, older and younger. Older is 11 and up, younger is 10 and below.

    Args:
        player_list (list): A list of tuples containing player names and ages.

    Returns:
        tuple: Two lists of tuples - older_players and younger_players.
    """
    older_players = [(name, age) for name, age in player_list if age > 10]
    younger_players = [(name, age) for name, age in player_list if age <= 10]

    return older_players, younger_players


def avg_age(player_list):
    """
    Calculates the average age of players in a list.

    Args:
        player_list (list): A list of tuples containing player names and ages.

    Returns:
        int: The rounded average age of the players.
    """
    total_age = sum(age for name, age in player_list)
    return round(total_age / len(player_list))


def find_min_max_ages(player_list):
    """
    Finds the minimum and maximum ages among players.

    Args:
        player_list (list): A list of tuples containing player names and ages.

    Returns:
        tuple: The minimum and maximum ages among players.
    """
    min_age, max_age = None, None

    for name, age in player_list:
        if min_age is None or age < min_age:
            min_age = age
        if max_age is None or age > max_age:
            max_age = age

    return min_age, max_age


def summary(team_name, roster, average_age, youngest_age, oldest_age):
    """
    Prints a summary of a team's player information.

    Args:
        team_name (str): The name of the team.
        roster (list): A list of tuples containing player names and ages.
        average_age (int): The average age of the players.
        youngest_age (int): The youngest player's age.
        oldest_age (int): The oldest player's age.
    """
    print(team_name)
    print(f"Total members: {len(roster)}")
    print(f"Average age: {average_age}")
    print(f"Youngest age: {youngest_age}")
    print(f"Oldest age: {oldest_age}")
    print("Members")

    for name, age in roster:
        print(f" - {name} {age}")


def main():
    # Collect player data and sort into teams
    total_roster = get_tuple_list("Enter player name: ", "Enter player age: ")
    bigs_roster, littles_roster = sort_by_age(total_roster)

    # Calculate metrics for each team
    bigs_avg = avg_age(bigs_roster)
    bigs_youngest, bigs_oldest = find_min_max_ages(bigs_roster)

    littles_avg = avg_age(littles_roster)
    littles_youngest, littles_oldest = find_min_max_ages(littles_roster)

    # Display team summaries
    summary("Team Bigs", bigs_roster, bigs_avg, bigs_youngest, bigs_oldest)
    summary("Team Littles", littles_roster, littles_avg, littles_youngest, littles_oldest)


if __name__ == '__main__':
    main()
