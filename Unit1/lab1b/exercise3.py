from byubit import Bit


def in_position(bit):
    bit.left()
    bit.move()
    bit.move()
    bit.move()
    bit.move()
    bit.move()
    bit.right()
    bit.move()
    bit.snapshot("In position")


def firework(bit):
    bit.paint('green')
    bit.right()
    bit.move()
    bit.move()
    bit.left()
    bit.move()
    bit.paint('green')
    bit.left()
    bit.move()
    bit.paint('red')
    bit.move()
    bit.right()
    bit.move()
    bit.paint('green')
    bit.snapshot("Firework")


def end_position(bit):
    bit.right()
    bit.move()
    bit.move()
    bit.move()
    bit.move()
    bit.move()
    bit.left()
    bit.move()
    bit.snapshot("End position")


@Bit.empty_world(5, 8)
def one_firework(bit):
    in_position(bit)
    firework(bit)
    end_position(bit)


if __name__ == '__main__':
    one_firework(Bit.new_bit)
