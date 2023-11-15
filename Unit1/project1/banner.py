from byubit import Bit


def banner(bit):
    """paint a column red, while the front is clear"""
    while not bit.is_green():
        bit.paint('red')
        bit.move()


def come_back(bit):
    bit.snapshot("found green square")
    """once the front is not clear, turn around"""
    bit.paint('red'), bit.left(), bit.left(), bit.snapshot("turning around")
    """move back down while the front is clear"""
    while bit.front_clear():
        bit.move()


@Bit.worlds("banner", "another_banner")
def run(bit):
    while bit:
        bit.left()
        bit.paint('red')
        banner(bit)
        come_back(bit)
        bit.left()
        if bit.front_clear():
            """"if front is clear, i.e., there's another column to do, move"""
            bit.snapshot("another column to do!")
            bit.move()
        else:
            """if not, break the loop, assuming all columns have been done"""
            bit.snapshot("all done!")
            break


if __name__ == '__main__':
    run(Bit.new_bit)
