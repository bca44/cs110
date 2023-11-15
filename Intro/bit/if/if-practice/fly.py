from byubit import Bit


def maybe_turn(bit):
    if bit.is_blue():
        bit.left(), bit.snapshot("left")
    elif bit.is_green():
        bit.right(), bit.snapshot("right")


@Bit.worlds('fly')
def run(bit):
    while not bit.is_red():
        bit.move(), bit.snapshot("move")
        maybe_turn(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
