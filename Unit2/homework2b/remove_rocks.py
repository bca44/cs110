from byubit import Bit


def move_until_green(bit):
    """tracks if safe to erase blue or no"""
    """returns true until lands on green square"""
    return not bit.is_green()


def erase_blue(bit):
    """moves forward until green square. removes blue squares on the way"""
    if bit.is_blue():
        bit.erase()


def go_to_end(bit):
    """advances until front not clear"""
    while bit.front_clear():
        bit.move()


@Bit.worlds('remove-rocks', 'remove-rocks2')
def run(bit):
    """first, moves to the strawberry patch, i.e., until green square"""
    while move_until_green(bit):
        bit.move()
    bit.move()
    """calls erase_blue(bit) until next green square"""
    while move_until_green(bit):
        erase_blue(bit)
        bit.move()
    go_to_end(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
