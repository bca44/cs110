from byubit import Bit


def detect_red(bit):
    """moves the cursor in a line until it lands on a red square"""
    while not bit.is_red():
        bit.move()


def make_trunk(bit):
    """turns left, then paints squares red until it lands in a green square"""
    bit.left()
    """make sure we don't repaint our square red"""
    bit.move()
    while not bit.is_green():
        bit.paint('red')
        bit.move()


@Bit.worlds('fix-tree', 'fix-another-tree')
def fix_the_tree(bit):
    detect_red(bit)
    make_trunk(bit)


if __name__ == '__main__':
    fix_the_tree(Bit.new_bit)
