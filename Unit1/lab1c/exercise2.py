from byubit import Bit


def move_til_red(bit):
    """moves until lands in red square"""
    while not bit.is_red():
        bit.move()


def blue_front(bit):
    """moves and paints blue while front clear"""
    while bit.front_clear():
        bit.move()
        bit.paint('blue')


@Bit.worlds('red-spot')
def go(bit):
    """go to red, u-turn, paint blue til end"""
    move_til_red(bit)
    bit.left()
    bit.move()
    bit.left()
    blue_front(bit)


if __name__ == '__main__':
    go(Bit.new_bit)
