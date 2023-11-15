import sys


def read_lines(filename):
    with open(filename) as file:
        return file.readlines()


def assign(name_list, slot_list):
    # assign first person to first slot, etc.
    name_slot_dict = {}

    for name, slot in zip(name_list, slot_list):
        name_slot_dict[name.strip()] = slot.strip()

    return name_slot_dict


def select_and_sum(a_dict):
    # takes user query, if person in dict, gives appointment details
    # else, says not assigned a timeslot
    while True:
        user_query = input("Name: ")
        if user_query == "":
            return
        elif user_query in a_dict:
            print(f"{user_query} is assigned {a_dict[user_query]}")
        else:
            print(f"{user_query} is not assigned a timeslot")


def main(name_file, timeslot_file):
    # assigns each person in the name_file to a time slot in the timeslot_file
    # assigns each person to the next available slot, in the order they are listed
    names = read_lines(name_file)
    timeslots = read_lines(timeslot_file)
    schedule_dict = assign(names, timeslots)
    select_and_sum(schedule_dict)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
