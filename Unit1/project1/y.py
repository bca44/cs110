from byubit import Bit


def paint_a_y(bit):
    bit.paint('blue')
    bit.move()
    bit.right()
    bit.move()
    bit.paint('blue')
    bit.move()
    bit.left()
    bit.move()
    bit.paint('blue')
    bit.right()
    bit.move()
    bit.paint('blue')
    bit.move()
    bit.paint('blue')
    bit.right()
    bit.right()
    bit.move()
    bit.move()
    bit.move()
    bit.right()
    bit.move()
    bit.paint('blue')
    bit.move()
    bit.left()
    bit.move()
    bit.paint('blue')
    bit.right()
    bit.move()
    bit.move()


@Bit.worlds('y')
def paint_2_ys(bit):
    paint_a_y(bit), bit.snapshot("first y")
    bit.move()
    paint_a_y(bit), bit.snapshot("second y")


if __name__ == '__main__':
    paint_2_ys(Bit.new_bit)
