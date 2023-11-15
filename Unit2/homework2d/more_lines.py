from byubit import Bit


def fill_line(bit, color):
    # fill in the spaces between two 'color' spaces
    # moves past the second colored marker
    bit.move()
    while bit.is_empty():
        bit.paint(color)
        bit.move()
    bit.snapshot("filled line")


def bit_return(bit):
    # takes bit to next row
    bit.left()
    bit.left()
    while bit.front_clear():
        bit.move()
    bit.right()
    bit.snapshot("returned bit")


@Bit.worlds('more-lines')
def run(bit):
    while bit.left_clear() or bit.front_clear():
        while bit.front_clear():
            if bit.is_empty():
                bit.move()
            else:
                color = bit.get_color()
                fill_line(bit, color)
                bit.move()
        bit_return(bit)
        if bit.front_clear():
            bit.move()
            bit.right()
        else:
            break
    # take bit to final spot
    bit.right()
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()


if __name__ == '__main__':
    run(Bit.new_bit)
