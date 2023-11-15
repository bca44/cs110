from byubit import Bit


def draw_one_dot(bit):
    """
    Draws one blue dot in the middle of a 3 x 3 square.
    Ends on the bottom right-hand corner of the square.
    """
    bit.move()
    bit.left()
    bit.move()
    bit.paint('blue')
    bit.right()
    bit.right()
    bit.move()
    bit.left()
    bit.move()


@Bit.empty_world(9, 3)
def draw_four_dots(bit):
    draw_one_dot(bit)
    draw_one_dot(bit)
    draw_one_dot(bit)
    draw_one_dot(bit)


if __name__ == '__main__':
    draw_four_dots(Bit.new_bit)
