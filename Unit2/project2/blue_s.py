from byubit import Bit

def make_s(bit):
    # makes an S in the outline the map gives

    # top half of S
    bit.left()
    blue_line(bit)

    bit.right()
    blue_line(bit)

    # top half painted, heads back to midpoint
    turn_around(bit)
    straight_line(bit)

    bit.left()
    straight_line(bit)

    # reaches midpoint
    bit.left()
    bit.move()
    bit.paint("blue")

    # bottom half of S
    bit.right()
    blue_line(bit)

    bit.right()
    blue_line(bit)

    turn_around(bit)
    straight_line(bit)

    bit.left()
    straight_line(bit)

    # back to midpoint, sets up to continue progressing 'east'
    bit.right()


def blue_line(bit):
    # paints blue in a straight line until blocked
    # including both the first and last squares

    while bit.front_clear():
        bit.paint("blue")
        bit.move()

    # catches last square
    bit.paint("blue")


def turn_around(bit):
    # turns bit around

    bit.left()
    bit.left()


def straight_line(bit):
    # moves bit straight until blocked. does not paint

    while bit.front_clear():
        bit.move()


@Bit.worlds('blue-s', 'big-blue-s')
def run(bit):

    while bit.front_clear():

        if not bit.is_green():
            bit.move()

        else:
            make_s(bit)
            bit.snapshot("made s")


if __name__ == '__main__':
    run(Bit.new_bit)
