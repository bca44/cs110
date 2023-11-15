def assign_teams(name_age, team_dict):
    """Return a list of (person, team) tuples"""

    name_team = []
    for name, age in name_age:
        nearest_multiple = (age // 3) * 3
        if nearest_multiple in team_dict:
            age = team_dict[nearest_multiple]
        else:
            age = "Adult League"
        name_team.append((name, age))

    return name_team


def print_teams(teams):
    for player, team in teams:
        print(f'{player} is on team {team}')


def main(participants, age_groups):
    teams = assign_teams(participants, age_groups)
    print_teams(teams)


if __name__ == '__main__':
    participants = [
        ('Joe', 14),
        ('Jane', 6),
        ('Johnny', 4),
        ('Jennifer', 20),
        ('Jack', 16),
        ('Janice', 2)
    ]

    age_groups = {
        0: 'Team Toddlers',
        3: 'Tiny Troupers',
        6: 'Starting Stars',
        9: 'Mighty Middles',
        12: 'Too Cool',
        15: 'Boundless'
    }

    main(participants, age_groups)
