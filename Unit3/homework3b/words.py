def play(secret_word):
    # word game - plays until player's guess equals word initially passed to play()

    while True:

        player_guess = input("Guess a word: ")

        if player_guess == secret_word:
            print("You got it!")
            break

    # gives player hints, based on the alphabetic position of the secret word
        elif player_guess > secret_word:
            print("Lower!")

        elif player_guess < secret_word:
            print("Higher!")


if __name__ == '__main__':
    play('python')
