from byubit import Bit


def make_column(bit, color):
    # turns left, makes a column of the given color
    # when front blocked, returns to original spot and orientation
    bit.left()
    bit.move()
    while bit.front_clear():
        bit.paint(color)
        bit.move()
    bit.paint(color)
    bit.left()
    bit.left()
    while bit.front_clear():
        bit.move()
    bit.left()


@Bit.worlds('color-bars', 'color-bars2')
def run(bit):
    while bit:
        if not bit.is_empty():
            color = bit.get_color()
            make_column(bit, color)
        if bit.front_clear():
            bit.move()
        else:
            break


if __name__ == '__main__':
    run(Bit.new_bit)
