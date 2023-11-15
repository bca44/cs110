from byubit import Bit


def line_up(bit):
    """
    moves up one square
    ends facing 'east'
    """
    bit.left()
    bit.move()
    bit.right()


def four_blues(bit):
    """
    paints the current square blue.
    moves two spaces, leaving one blank space between painted and current squares
    repeats three times
    """
    bit.paint('blue'), bit.move(), bit.move()
    bit.paint('blue'), bit.move(), bit.move()
    bit.paint('blue'), bit.move(), bit.move()
    bit.paint('blue')


def end(bit):
    """
    paints last square
    moves into 'ending position'
    """
    bit.right()
    bit.move()
    bit.left()


@Bit.empty_world(8, 3)
def dots(bit):
    line_up(bit)
    bit.snapshot("Lined up")
    four_blues(bit)
    bit.snapshot("Three blues")
    end(bit)
    bit.snapshot("Ending position")


if __name__ == '__main__':
    dots(Bit.new_bit)
