import random


def get_computer_choice():
    """
    Return a random choice of 'rock', 'paper', or 'scissors'
    """
    return random.choice(["rock", "paper", "scissors"])


def get_player_choice():
    while True:
        player = input('rock, paper, or scissors? ')
        if player == 'rock' or player == 'paper' or player == 'scissors':
            return player
        print("Not a valid choice! Try again!")


def do_winner(computer, player):
    if computer == player:
        print("Tie!")
        return 'tie'
    if computer == 'rock' and player == 'scissors':
        print("Rock smashes scissors! I win!")
        return 'computer'
    if computer == 'rock' and player == 'paper':
        print("Paper covers rock! You win!")
        return 'player'
    if computer == 'paper' and player == 'rock':
        print("Paper covers rock! I win!")
        return 'computer'
    if computer == 'paper' and player == 'scissors':
        print("Scissors cut paper! You win!")
        return 'player'
    if computer == 'scissors' and player == 'rock':
        print("Rock smashes scissors! You win!")
        return 'player'
    if computer == 'scissors' and player == 'paper':
        print("Scissors cut paper! I win!")
        return 'computer'


def react_to_result(result):
    if result == 'computer':
        print("🤑🤑🤑")
        return

    if result == 'player':
        print("😮‍💨😮‍💨😮‍💨")
        return

    print("🤨🤨🤨")


def play_again():
    response = input("Play again? (y/n) ")
    return response == 'y'


def play_game():
    while True:
        print("Welcome! Let's play rock, paper, scissors!")
        computer = get_computer_choice()
        print("I have my choice!")
        player = get_player_choice()
        result = do_winner(computer, player)
        react_to_result(result)
        if not play_again():
            return


if __name__ == '__main__':
    play_game()
