from byubit import Bit


def do_paint(bit):
    """tells main to paint red or no"""
    """paints all squares except red and empty ones"""
    if bit.is_red() or bit.is_empty():
        return False
    else:
        return True


@Bit.worlds('red-roses', 'red-roses2')
def run(bit):
    while bit.front_clear():
        if do_paint(bit):
            bit.paint("red")
            bit.move()
        else:
            bit.move()


if __name__ == '__main__':
    run(Bit.new_bit)
