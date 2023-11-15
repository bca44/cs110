from byubit import Bit


def three_reds(bit):
    bit.paint('red')
    bit.move()
    bit.paint('red')
    bit.move()
    bit.paint('red')
    bit.move()


@Bit.empty_world(7, 4)
def run(bit):
    three_reds(bit)
    bit.left()
    three_reds(bit)
    bit.right()
    three_reds(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
