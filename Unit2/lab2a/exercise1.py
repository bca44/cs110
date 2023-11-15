from byubit import Bit


def turn_or_change(bit):
    if bit.is_red():
        bit.left()
    elif bit.is_green():
        bit.paint('blue')
    elif bit.is_blue():
        bit.paint('green')


@Bit.worlds('exercise1')
def go(bit):
    while bit.front_clear():
        bit.move()
        turn_or_change(bit)


if __name__ == '__main__':
    go(Bit.new_bit)
