from byubit import Bit


def invert(bit):
    # makes blue blank and vice versa

    if bit.is_empty():
        bit.paint("blue")

    else:
        bit.erase()


def check_column(bit):
    # moves in a straight line, calling invert(bit) on each square, including the first and last

    bit.left()

    # catches the first square
    invert(bit)

    # inverts and moves in straight line til blocked
    while bit.front_clear():
        bit.move()
        invert(bit)

    bit.snapshot("column checked")


def back_down(bit):
    # turns around
    bit.left()
    bit.left()

    # moves bit back down
    while bit.front_clear():
        bit.move()

    bit.snapshot("back down")


@Bit.worlds('invert', 'invert2')
def run(bit):

    # runs through second to last column
    while bit.front_clear():
        check_column(bit)
        back_down(bit)

        # moves bit into bottom space of leftmost column
        bit.left()
        bit.move()

    # inverts last column
    check_column(bit)
    back_down(bit)

    # puts bit in proper orientation
    bit.left()


if __name__ == '__main__':
    run(Bit.new_bit)
