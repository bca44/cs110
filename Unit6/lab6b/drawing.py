def empty_grid(num_rows, num_columns, value=None):
    """
    Create an empty grid. <num_rows> is the number
    of rows in the grid. <num_columns> is the number
    of columns in the grid. Fill the grid with None or with
    whatever value the caller supplies in <value>.
    """
    # create an empty grid
    new_grid = []
    # keep going until we have created all the rows
    while len(new_grid) < num_rows:
        new_row = []
        # keep going until we have all the columns we need
        while len(new_row) < num_columns:
            # append an item for this column
            new_row.append(value)
        # now that we have a full row, append the row
        new_grid.append(new_row)
    return new_grid


def print_grid(grid, between=' '):
    """
    Print all the items in the grid, so that it looks like a grid.
    <between> is the character between columns, by default a space
    """
    for row in grid:
        for item in row:
            print(item, end=between)
        print()


def draw(grid, row, column, character):
    """
    <grid> - a grid
    <row> - a row number (integer)
    <column> - a column number (integer)
    <character> - a character

    Modifies the grid so that <row>,<column> contains <character>.
    Does not modify the grid if <row> is too small or too large.
    Also does not modify the grid if <column> is too small or too large.
    """
    grid[row][column] = character


def draw_on_grid(grid):
    """
    This function allows a user to draw on a grid. It does the following:
    - prints the grid, using '' as the character between columns
    - lets the user enter coordinates in "row, column" format, e.g.:
        2, 3
    - draws a 🟦 at each coordinate they enter
    - stops when they enter nothing
    """
    while True:
        print_grid(grid, between="")
        user_input = input("row, column: ")
        if user_input == "":
            break
        row, column = user_input.split(",")
        draw(grid, int(row), int(column), "🟦")


def main():
    # create an empty grid, using '⬜️' as the empty character
    grid = empty_grid(10, 10, '⬜️')
    # draw on the grid
    draw_on_grid(grid)


if __name__ == '__main__':
    main()
