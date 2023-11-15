from byubit import Bit


def cond(bit):
    if bit.is_empty():
        bit.paint("red"), bit.snapshot("empty")
    elif bit.is_green():
        bit.left(), bit.snapshot("green")
    elif bit.is_blue():
        bit.right(), bit.snapshot("blue")
    elif bit.is_red():
        bit.snapshot("red")
        pass


@Bit.worlds('wander', 'wander2')
def go(bit):
    bit.paint("red")
    while bit.front_clear():
        bit.move()
        cond(bit)


if __name__ == '__main__':
    go(Bit.new_bit)
