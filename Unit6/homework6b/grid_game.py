import sys


def read_grid(filename):
    """
    Read the file as a grid

    Each line becomes a row.
    Spaces delineate each value within a row.
    """
    with open(filename) as file:
        return [line.split() for line in file.readlines()]


def print_grid(grid):
    """
    Print the grid with spaces between each value and newlines between each row
    """
    # go through all the rows
    for row in grid:
        for item in row:
            # print the item, but with a space after it, not a newline
            print(item, end=' ')
        print()


def get_input():
    response = input("Action: ")
    while response not in ["u", "d", "l", "r"]:
        print("Invalid action. Please try again using 'u', 'r', 'l', or 'r'.")
        response = input("Action: ")
    return response


def get_coordinates(current_row, current_column, player_action):
    """
    calculates new row, column values based on current location and player action
    """
    new_row, new_column = 0, 0
    if player_action == "u":
        new_row = current_row - 1
        new_column = current_column
    elif player_action == "d":
        new_row = current_row + 1
        new_column = current_column
    elif player_action == "l":
        new_row = current_row
        new_column = current_column - 1
    elif player_action == "r":
        new_row = current_row
        new_column = current_column + 1

    return new_row, new_column


def is_blocked(grid, row, col, blocked_value):
    """
    Return True if the value at row, col in the grid is the blocked_value

    Also return True if the row, col coordinate is out of bounds.
    """
    rows, cols = len(grid), len(grid[0])

    if grid[row][col] == blocked_value or not (0 <= row < rows and 0 <= col < cols):
        return True
    return False


def update_grid(grid, old_row, old_col, new_row, new_col, empty=None):
    """
    Move the value at old_row, old_col to new_row, new_col

    Fill the cell at old_row, old_col with the empty value

    Returns True if the game is won, False if not.
    """
    new_value = grid[new_row][new_col]

    grid[old_row][old_col] = empty
    grid[new_row][new_col] = "@"

    return new_value == "!"


def main(grid_file):
    """
    presents player with current view of map (print_grid)
    accepts player input {u:up, d:down, l:left, r:right}
    moves "@" according to input unless:
        "@" would move out bounds. "@" does not move
        "@" would move onto space marked by "*". "@" does not move
    repeat above until "@" reaches "!"
    """

    # read in grid
    grid = read_grid(grid_file)
    old_row, old_column = 0, 0

    while True:
        # show player map
        print_grid(grid)

        # take player input
        player_input = get_input()

        # uses player input to calculate new_row, new_column
        new_row, new_column = get_coordinates(old_row, old_column, player_input)

        # if space at new_row, new_column open:
        if not is_blocked(grid, new_row, new_column, "*"):
            # move "@"
            win_value = update_grid(grid, old_row, old_column, new_row, new_column, ".")
            # if "@" replaces "!", shows final grid and prints message
            if win_value:
                print_grid(grid)
                print("You win!")
                break
            # update old row, column variables
            old_row, old_column = new_row, new_column


if __name__ == '__main__':
    main(sys.argv[1])
