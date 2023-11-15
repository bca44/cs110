from byubit import Bit


def pallet(bit):
    """paints two red squares in a row."""
    bit.paint('red')
    bit.move()
    bit.paint('red')
    bit.snapshot('pallet')


def box(bit):
    """makes a left-adjusted 2 x 2 blue square"""
    bit.paint('blue')
    bit.move()
    bit.paint('blue')
    reset(bit)
    bit.paint('blue')
    bit.move()
    bit.paint('blue')
    bit.snapshot('box')


def reset(bit):
    """takes the bit cursor to the leftmost box on the next line-up, cursor facing east"""
    bit.left()
    bit.move()
    bit.left()
    bit.move()
    bit.left()
    bit.left()
    bit.snapshot('reset')


def pallet_box(bit):
    """puts a 2 x 2 blue box on top of a 1 x 2 red pallet"""
    pallet(bit)
    reset(bit)
    box(bit)
    reset(bit)


@Bit.empty_world(3, 10)
def boxes(bit):
    pallet_box(bit)
    pallet_box(bit)
    pallet_box(bit)


if __name__ == '__main__':
    boxes(Bit.new_bit)
