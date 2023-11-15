from byubit import Bit


def least_resistance(bit):
    """finds path of least resistance, done when lands in red square"""
    """tries front, then left, then right"""
    """paints every square traversed green"""
    while not bit.is_red():
        if bit.front_clear():
            bit.paint('green')
            bit.move(), bit.snapshot("front")
        elif bit.left_clear():
            bit.paint('green')
            bit.left()
            bit.move(), bit.snapshot("left")
        else:
            # elif bit.right_clear():
            bit.paint('green')
            bit.right()
            bit.move(), bit.snapshot("right")


@Bit.worlds('maze')
def solve_maze(bit):
    least_resistance(bit)


if __name__ == "__main__":
    solve_maze(Bit.new_bit)
