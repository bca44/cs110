def make_empty_grid(num_rows, num_columns, value=None):
    new_grid = []
    for row in range(num_rows):
        new_row = []
        for column in range(num_columns):
            new_row.append(value)
        new_grid.append(new_row)
    return new_grid


def print_grid(grid: list[list]):
    for row in grid:
        for item in row:
            print(item, end=' ')
        print()


def main():
    # (3) Create an empty grid, 5 rows and 8 columns
    # use a space as the value for the grid
    empty_grid = make_empty_grid(5, 8, " ")
    # (4) put a '🦋' in (1, 1) -- row 1 -- column 1
    empty_grid[1][1] = "🦋"
    # (5) put a '🦖' in (0, 7)
    empty_grid[0][7] = "🦖"
    # (6) put a '🐳' in (4, 2)
    empty_grid[4][2] = "🐳"
    # (7) print the grid
    print_grid(empty_grid)


if __name__ == '__main__':
    main()
