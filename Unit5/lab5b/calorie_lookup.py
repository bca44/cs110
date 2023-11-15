import sys


def readlines(filename):
    """
    Reads the file with the given filename and
    returns a list of lines in the file.
    """
    with open(filename) as f:
        return f.readlines()


def read_csv(filename):
    """
    Reads the CSV file with the given filename. It should
    have lines that are of the format "food,calories". This
    function returns a dictionary that maps food -> calories.
    """
    food_cal_dict = {}

    for line in readlines(filename):
        food, cal = line.split(",")
        food_cal_dict[food] = cal

    return food_cal_dict


def input_loop(foods):
    """
    Allows a person to enter a food and then prints out the calories
    in one serving of that food.
    """
    while True:
        # get the food
        food = input("Food: ")
        if food == '':
            # stop if the entry is empty
            return
        if food in foods:
            # if the food is in the dictionary, print out info about
            # its calories per serving
            calories = foods[food]
            print(f"{food} has {calories} calories per serving")
        else:
            # otherwise, tell the person this food is not in the database
            print(f"{food} is not in our database")


def main(infile):
    foods = read_csv(infile)
    input_loop(foods)


if __name__ == '__main__':
    main(sys.argv[1])
