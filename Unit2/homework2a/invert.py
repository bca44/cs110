from byubit import Bit


def invert(bit):
    """paints empty squares blue, erases blue squares"""
    """does nothing on other squares"""
    if bit.is_empty():
        bit.paint('blue')
    elif bit.is_blue():
        bit.erase()
    else:
        pass


@Bit.worlds('invert', 'invert2', 'invert-careful')
def go(bit):
    while bit:
        invert(bit)
        """moves bit if front clear. otherwise, breaks the loop"""
        if bit.front_clear():
            bit.move()
        else:
            break


if __name__ == '__main__':
    go(Bit.new_bit)
