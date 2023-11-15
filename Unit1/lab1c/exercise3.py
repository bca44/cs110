from byubit import Bit


def blue_front(bit):
    """moves and paints blue while front clear"""
    while bit.front_clear():
        bit.move()
        bit.paint('blue')


@Bit.empty_world(5, 3)
def go(bit):
    bit.paint('red')
    bit.move()
    bit.paint('green')
    blue_front(bit)


if __name__ == '__main__':
    go(Bit.new_bit)
