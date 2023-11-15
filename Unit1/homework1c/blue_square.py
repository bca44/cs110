from byubit import Bit


# Something isn't working right. Fix it!
@Bit.worlds('blue-square')
def go(bit):
    # Draw a square
    while not bit.is_blue():
        bit.paint("blue")
        bit.move()
        bit.paint("blue")
        bit.move()
        bit.right()
        bit.snapshot("loop done")


if __name__ == '__main__':
    go(Bit.new_bit)
