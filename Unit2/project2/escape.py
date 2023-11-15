from byubit import Bit


def pick_up_gem(bit):
    # picks up gem, returns 'color' so run(bit) knows what bit picked up

    color = bit.get_color()
    bit.paint("blue")

    return color


def escape(bit):
    # gets bit out of the cave
    # cycles through front, right, and left options to not move into error

    bit.paint("blue")

    if bit.front_clear():
        bit.move()

    elif bit.right_clear():
        bit.right()
        bit.move()

    elif bit.left_clear():
        bit.left()
        bit.move()


def climb(bit):
    # bit climbs the green wall

    while bit.is_green():
        bit.move()


def leave_stone(bit, color):
    # gets bit to final position, deposits gemstone, using 'color' from run(bit)

    bit.right()
    bit.move()
    bit.paint(color)
    bit.move()


@Bit.worlds('escape', 'escape2')
def run(bit):
    gem_type = pick_up_gem(bit)

    while not bit.is_green():
        escape(bit)
    bit.snapshot("escaped!")

    bit.left()
    climb(bit)
    bit.snapshot("climbed!")

    leave_stone(bit, gem_type)
    bit.snapshot("done!")


if __name__ == '__main__':
    run(Bit.new_bit)
