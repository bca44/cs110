from byubit import Bit


def keep_spiraling(bit):
    """gives the 'ok' to keep spiraling or not"""
    """continues until lands back in non-empty square"""
    if bit.front_clear():
        return bit.is_empty()
    else:
        """if front not clear, turns left"""
        bit.left()
        return bit.is_empty()


@Bit.worlds('paint-the-box', 'paint-another-box')
def run(bit):
    while keep_spiraling(bit):
        bit.paint("green")
        bit.move()


if __name__ == '__main__':
    run(Bit.new_bit)
