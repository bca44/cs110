from byubit import Bit


def go_up(bit):
    while not bit.right_clear():
        """gets bit to top. goes forward and marks green when possible"""
        """if front blocked, calls jump_up(bit)"""
        if not bit.front_clear():
            jump_up(bit)
        bit.move()
        plant_tree(bit)


def jump_up(bit):
    """while right blocked, turns left and moves up. when done turns back right"""
    bit.left()
    while not bit.right_clear():
        bit.move()
    bit.right()


def plant_tree(bit):
    """paints green if square below is black"""
    if not bit.right_clear():
        bit.paint("green")


def go_down(bit):
    """takes bit down while front is clear"""
    """if right clear, calls jump_down(bit)"""
    while bit.front_clear():
        if bit.right_clear():
            jump_down(bit)
        plant_tree(bit)
        bit.move()


def jump_down(bit):
    """takes bit down a ledge. moves while front clear"""
    bit.right()
    while bit.front_clear():
        bit.move()
    bit.left()


@Bit.worlds('y-mountain', 'mountain')
def run(bit):
    bit.paint('green')
    go_up(bit)
    go_down(bit)
    bit.paint('green')


if __name__ == '__main__':
    run(Bit.new_bit)
