from byubit import Bit


def hull(bit):
    bit.left()  # first the hull
    bit.move()
    bit.paint("blue")
    bit.right()
    bit.move()
    bit.right()
    bit.move()
    bit.paint("blue"), bit.left()
    bit.move(), bit.paint("blue")
    bit.move(), bit.paint("blue")
    bit.move(), bit.paint("blue")
    bit.move(), bit.paint("blue")
    bit.move(), bit.paint("blue")
    bit.move(), bit.left()
    bit.move(), bit.paint("blue")
    bit.snapshot("End of hull")


def mast(bit):
    bit.left(), bit.move(), bit.move()  # now the mast
    bit.move(), bit.paint("red")
    bit.move(), bit.paint("red")
    bit.right(), bit.move(), bit.paint("red")
    bit.right(), bit.move(), bit.paint("red")
    bit.left(), bit.move(), bit.paint("red")
    bit.left(), bit.move(), bit.paint("red")
    bit.right(), bit.move(), bit.paint("red")
    bit.right(), bit.move(), bit.paint("red")
    bit.left(), bit.move(), bit.paint("red")
    bit.left(), bit.move(), bit.paint("red")
    bit.right(), bit.move(), bit.paint("red")
    bit.right(), bit.move(), bit.paint("red")  # and now for the sail
    bit.snapshot("End of mast")


def sail(bit):
    bit.left(), bit.left(), bit.move(), bit.move()
    bit.paint("green"), bit.move()
    bit.left(), bit.move()
    bit.paint("green")
    bit.move(), bit.left(), bit.move(), bit.paint("green")
    bit.snapshot("End of sail")


@Bit.empty_world(8, 8)
def picasso(bit):  # it's a sailboat!
    hull(bit)
    mast(bit)
    sail(bit)


if __name__ == "__main__":
    picasso(Bit.new_bit)
