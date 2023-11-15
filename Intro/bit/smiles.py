from byubit import Bit


@Bit.empty_world(25, 6)
def all_smiles(bit):
    smile(bit)
    reset(bit)
    smile(bit)
    reset(bit)
    smile(bit)
    reset(bit)
    smile(bit)


def smile(bit):
    bit.left(), bit.move(), bit.move(), bit.move(), bit.move()
    bit.right(), bit.move(), bit.paint("blue")
    bit.right(), bit.move(), bit.move(), bit.paint("blue")
    bit.move(), bit.left()
    bit.move(), bit.paint("blue")
    bit.move(), bit.paint("blue")
    bit.move(), bit.paint("blue")
    bit.move(), bit.left()
    bit.move(), bit.paint("blue")
    bit.move(), bit.move(), bit.paint("blue")
    bit.right()
    bit.snapshot("Smile completed")


def reset(bit):
    bit.right(), bit.move(), bit.move(), bit.move(), bit.move()
    bit.left(), bit.move()
    bit.snapshot("Reset")


if __name__ == '__main__':
    all_smiles(Bit.new_bit)
