from byubit import Bit


def move_to_tree(bit):
    """ Moves to the trunk """
    bit.move()
    bit.move()
    bit.snapshot("move_to_tree")


def draw_trunk(bit):
    """ Draws the trunk (two red squares)  """
    bit.left()
    bit.paint('red')
    bit.move()
    bit.paint('red')
    bit.snapshot("draw_trunk")


def draw_branches(bit):
    """ Draws the branches """
    bit.move()
    bit.paint('green')
    bit.left()
    bit.move()
    bit.paint('green')
    bit.right()
    bit.move()
    bit.right()
    bit.move()
    bit.paint('green')
    bit.move()
    bit.right()
    bit.move()
    bit.paint('green')
    bit.snapshot("draw_branches")


def go_back_down(bit):
    """ Moves back down to the ground, below the right-most branch, facing east. """
    bit.move()
    bit.move()
    bit.left()
    bit.snapshot("go_back_down")


def one_tree(bit):
    move_to_tree(bit)
    draw_trunk(bit)
    draw_branches(bit)
    go_back_down(bit)


@Bit.empty_world(13, 4)
def trees(bit):
    one_tree(bit)
    bit.move()
    one_tree(bit)
    bit.move()
    one_tree(bit)


if __name__ == '__main__':
    trees(Bit.new_bit)
