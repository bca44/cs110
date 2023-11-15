from byubit import Bit


def freedom(bit):
    return bit.left_clear() and bit.right_clear()


@Bit.worlds('freedom')
def go(bit):
    while not freedom(bit):
        bit.move()


if __name__ == '__main__':
    go(Bit.new_bit)
