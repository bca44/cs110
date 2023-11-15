from byubit import Bit


def fill_field(bit):
    get_to_bottom(bit)
    while bit.front_clear():
        fill_column(bit)
        bit.move()
    fill_column(bit)
    find_space(bit)


def get_to_bottom(bit):
    """takes bit to the bottom of the first column, facing 'north'"""
    bit.move()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()
    bit.snapshot("get to bottom")


def fill_column(bit):
    """fills in columns"""
    bit.left()
    bit.paint("green")
    while bit.front_clear():
        bit.move()
        bit.paint("green")
    bit.left(), bit.left()
    while bit.front_clear():
        bit.move()
    bit.left()
    bit.snapshot("fill column")


def find_space(bit):
    bit.left()
    while not bit.right_clear():
        bit.move()
    bit.right()
    bit.move()
    bit.snapshot("found entrance")


@Bit.worlds('soccer', 'soccer2')
def go(bit):
    while bit:
        if bit.front_clear():
            fill_field(bit)
        else:
            bit.snapshot("all done")
            break


if __name__ == '__main__':
    go(Bit.new_bit)
