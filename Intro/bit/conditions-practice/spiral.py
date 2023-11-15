from byubit import Bit


def keep_spiraling(bit):
    """continues the spiral while true, i.e., if front or left clear"""
    if bit.front_clear():
        return True
    elif bit.left_clear():
        """if only left clear, turns left before continuing"""
        bit.left()
        return True
    else:
        """if both front and left blocked, fills in last square, breaks"""
        bit.paint("blue")
        return False


@Bit.worlds('spiral')
def run(bit):
    while keep_spiraling(bit):
        """while true, continues spiraling - paints squares blue, moves"""
        bit.paint("blue")
        bit.move()


if __name__ == '__main__':
    run(Bit.new_bit)
