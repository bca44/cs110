from byubit import Bit


@Bit.empty_world(3,3)
def do_stuff(bit):
    bit.move()
    bit.paint("blue")
    bit.left()
    bit.move()
    bit.paint("blue")
    bit.move()
    bit.left()
    bit.move()
    bit.paint("blue")
    bit.right()
    bit.right()
    bit.move()
    bit.move()
    bit.paint("blue")



if __name__ == 'main':
    do_stuff(Bit.new_bit)