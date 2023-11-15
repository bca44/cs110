from byubit import Bit


def empty_cond(bit):
    """moves bit past an empty square"""
    if bit.is_empty():
        bit.move(), bit.snapshot("empty square")


def green_cond(bit):
    """'plants' a red square on top of a green square bit lands on"""
    if bit.is_green():
        bit.left()
        bit.move()
        bit.paint('red')
        """moves bit past green square in original direction"""
        bit.left(), bit.left()
        bit.move()
        bit.left()
        bit.move(), bit.snapshot("flower planted")


@Bit.worlds('flowers')
def go(bit):
    while bit.front_clear():
        empty_cond(bit)
        green_cond(bit)


if __name__ == '__main__':
    go(Bit.new_bit)
