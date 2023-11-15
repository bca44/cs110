from byubit import Bit


def gem_pool(bit):
    # takes the current square color, erases it, and fills a pool with the color
    color = bit.get_color()
    bit.erase()

    # gets over the pool's edge, moves to top left square
    while not bit.right_clear():
        bit.move()

    bit.right()
    bit.move()
    bit.left()

    # fills columns, stops before the last one
    while bit.front_clear():
        fill_column(bit, color)
        return_to_pool_top(bit)
        move_to_column_start(bit)

    # fills last column
    fill_column(bit, color)
    return_to_pool_top(bit)
    bit.snapshot("filled gem pool")


def fill_column(bit, color):
    # fills column with given color

    bit.right()

    while bit.front_clear():
        bit.paint(color)
        bit.move()

    # paints the last one too
    bit.paint(color)
    bit.snapshot("filled column")


def return_to_pool_top(bit):
    # takes bit to top of pool column, turns left

    # turns around
    bit.left()
    bit.left()

    # goes straight til blocked
    while not bit.is_empty():
        bit.move()

    bit.right()

    # ends one square above top right square in pool
    bit.snapshot("returned")


def move_to_column_start(bit):
    # moves bit from where return_to_pool_top ends to starting spot for fill_column

    bit.move()
    bit.right()
    bit.move()
    bit.left()

    bit.snapshot("top of column")


@Bit.worlds('gems', 'gems2')
def run(bit):
    while bit.front_clear():

        if bit.is_empty():
            bit.move()

        else:

            gem_pool(bit)
            bit.move()


if __name__ == '__main__':
    run(Bit.new_bit)
