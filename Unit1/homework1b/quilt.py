from byubit import Bit


def red_line(bit):
    """paints three squares red in a 1 x 3 rectangle"""
    bit.paint('red')
    bit.move()
    bit.paint('red')
    bit.move()
    bit.paint('red')
    bit.snapshot('red line')


def green_square(bit):
    """paints a 3 x 3 green square, except the middle is blue"""
    three_green(bit)
    reset(bit)
    g_b_g(bit)
    reset(bit)
    three_green(bit)
    bit.snapshot('green square')


def three_green(bit):
    """paints three squares green in a 1 x 3 rectangle"""
    bit.paint('green')
    bit.move()
    bit.paint('green')
    bit.move()
    bit.paint('green')


def g_b_g(bit):
    """paints a 1 x 3 rectangle, with a blue square between two green ones"""
    bit.paint('green')
    bit.move()
    bit.paint('blue')
    bit.move()
    bit.paint('green')

def reset(bit):
    """takes the cursor down three and right one, facing north"""
    bit.left()
    bit.left()
    bit.move()
    bit.move()
    bit.left()
    bit.move()
    bit.left()
    bit.snapshot('reset')


def pattern(bit):
    """makes the 4 x 4 pattern repeated in the quilt"""
    red_line(bit)
    reset(bit)
    green_square(bit)
    reset(bit)
    bit.snapshot('pattern')


def final_spot(bit):
    """puts the cursor in its final spot"""
    bit.left()
    bit.left()
    bit.move()
    bit.move()
    bit.left()


@Bit.empty_world(13,3)
def make_a_quilt(bit):
    bit.left()
    pattern(bit)
    pattern(bit)
    pattern(bit)
    red_line(bit)
    final_spot(bit)


if __name__ == '__main__':
    make_a_quilt(Bit.new_bit)
