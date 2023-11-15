from byubit import Bit


def go_to_color(bit):
    """paints emtpy squares green and moves"""
    """stops when it lands in a non-empty square"""
    while bit.is_empty():
        bit.paint('green')
        bit.move()


@Bit.worlds('go-to-lake', 'go-to-another-lake')
def go(bit):
    go_to_color(bit), bit.snapshot("go to the stop sign")
    bit.left(), bit.snapshot("turn left at the stop sign")
    bit.move(), bit.snapshot("move into an empty square")
    go_to_color(bit), bit.snapshot("go to the lake")


if __name__ == "__main__":
    go(Bit.new_bit)
