from byubit import Bit


def walk_to_ocean(bit):
    """move straight until the 'shore' ends"""
    while not bit.right_clear():
        bit.move()


def search(bit):
    """move until in a red square, then paint red"""
    while not bit.is_red():
        bit.move()
    while bit.is_red():
        bit.paint('blue')


@Bit.worlds('dive-for-treasure', 'dive-for-deep-treasure')
def dive(bit):
    walk_to_ocean(bit), bit.snapshot("made it to the ocean")
    bit.right()
    search(bit), bit.snapshot("found it! all done")


if __name__ == "__main__":
    dive(Bit.new_bit)
