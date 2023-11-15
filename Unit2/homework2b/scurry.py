from byubit import Bit


def paint(bit):
    """paint conditions: paints empty squares green, paints green squares blue"""
    if bit.is_empty():
        bit.paint('green')
    elif bit.is_green():
        bit.paint("blue")


def scurry(bit):
    """move order: prefers front. if not available, takes left or right"""
    if bit.front_clear():
        bit.move()
    elif bit.left_clear():
        bit.left()
        bit.move()
    elif bit.right_clear():
        bit.right()
        bit.move()


@Bit.worlds('scurry', 'scurry2')
def go(bit):
    while bit.front_clear() or bit.right_clear() or bit.left_clear():
        paint(bit)
        scurry(bit)
    bit.paint("green")


if __name__ == '__main__':
    go(Bit.new_bit)
