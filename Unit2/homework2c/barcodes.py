from byubit import Bit


def fill_column(bit):
    """fills in columns that are marked with blue squares"""
    if bit.is_blue():
        bit.left()
        while bit.front_clear():
            bit.move()
            bit.paint("blue")
        bit.left(), bit.left()
        while bit.front_clear():
            bit.move()
        bit.left()
        bit.snapshot("Fill column")


def ok_to_move(bit):
    """gives the ok to move or no"""
    return bit.front_clear()


def barcode(bit):
    """calls fill columns to fill in the barcode"""
    """calls ok to move to avoid going out of bounds"""
    while bit:
        fill_column(bit)
        if ok_to_move(bit):
            bit.move(), bit.snapshot("ok to move")
        else:
            bit.snapshot("all done!")
            break


@Bit.worlds('barcode', 'barcode2')
def run(bit):
    barcode(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
