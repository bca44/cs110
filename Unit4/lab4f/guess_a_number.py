import random


def pick_number():
    """
    Returns a random number between 1 and 100
    """
    return random.randint(1, 100)


def guess(number):
    while True:
        your_number = int(input("Guess: "))
        # "You got it!" if correct
        # "Lower" if too high
        # "Higher if too low
        if number == your_number:
            print("You got it!")
            return
        elif number > your_number:
            print("Higher")
        else:
            print("Lower")


def play_game():
    print("Welcome! I picked a number between 1 and 100. Can you guess it?")
    number = pick_number()
    guess(number)


if __name__ == '__main__':
    play_game()
