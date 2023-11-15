from byubit import Bit


def follow_rules(bit):
    if bit.is_blue():
        bit.left()
    elif bit.is_green():
        bit.right()
    elif bit.is_red():
        bit.right()
        bit.right()


@Bit.worlds('exercise2')
def go(bit):
    while bit.front_clear():
        bit.move()
        follow_rules(bit)


if __name__ == '__main__':
    go(Bit.new_bit)
