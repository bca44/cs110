from byubit import Bit


def make_vine(bit):
    bit.left()
    while bit.front_clear():
        bit.move()
        bit.paint("green")
    bit.left()
    bit.left()
    while bit.front_clear():
        bit.move()
    bit.left()
    bit.snapshot("vine made")


def fill_well(bit):
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()
    bit.left()
    while not bit.right_clear():
        bit.paint("blue")
        bit.move()
    bit.right()
    bit.snapshot("well filled")


@Bit.worlds('wells-and-vines')
def run(bit):
    while bit.front_clear():
        if bit.is_green():
            make_vine(bit)
            bit.move()
        elif bit.right_clear():
            fill_well(bit)
            bit.move()
        elif bit.is_empty():
            bit.move()


if __name__ == '__main__':
    run(Bit.new_bit)
