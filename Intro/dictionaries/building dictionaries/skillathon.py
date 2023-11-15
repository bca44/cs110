def make_room_assignments(speakers, rooms):
    """
    returns a dictionary mapping each speaker to a room
    """
    assignments = {}

    for speaker, room in zip(speakers, rooms):
        assignments[speaker] = room

    return assignments


def make_itinerary(name_time_list, name_room_dict):
    """
    desired_speaker_times: list of (speaker, time) tuples
    room_assignments: a dictionary that maps speakers to rooms
    Return a list of (speaker, room, time) tuples
    """
    name_room_time = []

    for name, time in name_time_list:
        name_room_time.append((name, name_room_dict[name], time))

    return name_room_time


def invert_assignments(a_dict):
    """
    returns a new dictionary, where each key-value pair is inverted
    """
    inverted_dict = {}

    for key, value in a_dict.items():
        inverted_dict[value] = key

    return inverted_dict


if __name__ == "__main__":

    speaker_list = ['Page', 'Jones', 'Bean', 'Zappala', 'Clement', 'Fulda']
    room_list = ['2233', '2228', '2230', '2242', '2220', '2238']
    desired_lineup = [("Fulda", "9am"), ("Page", "10am"), ("Jones", "11am"), ("Zappala", "12pm")]

    # {'Page': '2233', 'Jones': '2228', 'Bean': '2230', 'Zappala': '2242', 'Clement': '2220', 'Fulda': '2238'}
    speaker_room_dict = make_room_assignments(speaker_list, room_list)

    # [('Fulda', '2238', '9am'), ('Page', '2233', '10am'), ('Jones', '2228', '11am'), ('Zappala', '2242', '12pm')]
    itinerary = make_itinerary(desired_lineup, speaker_room_dict)

    # {'2233': 'Page', '2228': 'Jones', '2230': 'Bean', '2242': 'Zappala', '2220': 'Clement', '2238': 'Fulda'}
    room_speaker_dict = invert_assignments(speaker_room_dict)
