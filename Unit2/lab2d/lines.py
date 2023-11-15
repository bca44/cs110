from byubit import Bit


def paint_row(bit):
    while bit.front_clear():
        if bit.is_empty():
            bit.move()
            bit.snapshot("empty")
        else:
            color = bit.get_color()
            bit.move()
            while bit.is_empty() and bit.front_clear():
                bit.paint(color)
                bit.move()
                bit.snapshot("painted")


def go_back(bit):
    bit.left()
    bit.left()
    while bit.front_clear():
        bit.move()
    bit.left()
    bit.left()


@Bit.worlds('lines')
def run(bit):
    while bit.front_clear():
        paint_row(bit)
        go_back(bit)
        bit.left()
        if bit.front_clear():
            bit.move()
            bit.right()


if __name__ == '__main__':
    run(Bit.new_bit)
