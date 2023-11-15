from byubit import Bit


def paint_column(bit):
    """paint a column green, while the front is clear"""
    while bit.front_clear():
        bit.move()
        bit.paint('green')


def come_back(bit):
    """move back down while the front is clear"""
    bit.left(), bit.left()
    while bit.front_clear():
        bit.move()
    bit.left()


@Bit.worlds("grassy_field", "big_grassy_field")
def run(bit):
    while bit:
        bit.left()
        bit.paint('green')
        paint_column(bit), bit.snapshot("paint column")
        come_back(bit), bit.snapshot("come back")
        if bit.front_clear():
            bit.move(), bit.snapshot("another column")
        else:
            bit.snapshot("all done!")
            break



if __name__ == '__main__':
    run(Bit.new_bit)
