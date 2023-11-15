from byubit import Bit


def bg(bit):
    """determines if green square needs erased or no"""
    """if green and left or right not clear, needs erased"""
    if bit.is_green() and not bit.left_clear():
        return True
    elif bit.is_green() and not bit.right_clear():
        return True
    else:
        return False


@Bit.worlds('clear-green', 'clear-green2')
def run(bit):
    """runs until the 'wall', asks bg(bit) if needs erased or no"""
    while bit.front_clear():
        if bg(bit):
            bit.erase()
            bit.move()
        else:
            bit.move()


if __name__ == '__main__':
    run(Bit.new_bit)
