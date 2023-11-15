from byubit import Bit


def to_stem(bit):
    while bit.is_empty():
        bit.move()
    color = bit.get_color()
    while bit.is_empty():
        bit.move()
    return color


def paint_bud(bit, color):
    bit.left()
    while not bit.is_empty():
        bit.move()
    bit.paint(color)
    bit_return(bit)


def bit_return(bit):
    bit.left(), bit.left()
    while bit.front_clear():
        bit.move()


@Bit.worlds('flowers1', 'flowers2')
def run(bit):
    while bit.front_clear():
        color = to_stem(bit)
        paint_bud(bit, color)


if __name__ == '__main__':
    run(Bit.new_bit)
