from byubit import Bit


def surround(bit):
    """makes a green square shape, without the corner pieces."""
    """when it circles back to itself, breaks"""
    one_side(bit)
    turn(bit)


def one_side(bit):
    """paints squares green until right side clear"""
    while not bit.right_clear():
        bit.paint('green')
        bit.move()


def turn(bit):
    """turns corner of green 'square' without painting"""
    bit.right()
    bit.move()


@Bit.worlds('surround', 'surround2')
def run(bit):
    while bit.front_clear():
        if bit.right_clear() or bit.is_green():
            bit.move()
        else:
            surround(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
