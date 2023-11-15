from byubit import Bit


def to_pool(bit):
    """take bit to the edge of the pool"""
    while (not bit.right_clear()) and bit.front_clear():
        bit.move()


def fill_pool(bit):
    """fills pool in one column increments, ends when front not clear"""
    while bit.right_clear():
        pool_column(bit)
        back_up(bit)
        bit.move()
    if bit.front_clear():
        flower(bit)


def pool_column(bit):
    """makes each individual pool column"""
    bit.right()
    while bit.front_clear():
        bit.move()
        bit.paint("blue")
    bit.snapshot("pool column")


def back_up(bit):
    bit.left(), bit.left()
    while bit.is_blue():
        bit.move()
    bit.right()


def flower(bit):
    """paints a flower on the black square immediately past the pool"""
    bit.left()
    bit.paint("green"), bit.move(), bit.paint("green")
    bit.left(), bit.move()
    bit.right(), bit.move()
    bit.paint("red"), bit.right()
    bit.move(), bit.paint("red"), bit.move(), bit.paint("red")
    bit.left(), bit.move()
    bit.left(), bit.move(), bit.paint("red")
    bit.left()
    bit.move(), bit.move(), bit.move()
    bit.left()


@Bit.worlds('blossoms', 'blossoms2')
def go(bit):
    while bit.front_clear():
        to_pool(bit)
        fill_pool(bit)


if __name__ == '__main__':
    go(Bit.new_bit)
