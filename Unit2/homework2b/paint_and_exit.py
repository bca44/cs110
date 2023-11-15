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


def leave(bit):
    """false when lands on green square"""
    """continues when front or right clear"""
    if bit.is_green():
        return False
    elif bit.front_clear():
        return True
    elif bit.right_clear():
        bit.right()
        return True


@Bit.worlds('paint-and-exit', 'paint-and-exit2')
def run(bit):
    """paints the 'room' first"""
    while keep_spiraling(bit):
        bit.paint("blue")
        bit.move()
    """sets up to 'leave'"""
    bit.right(), bit.right()
    bit.move()
    """"moves while leave True, ends when false (lands on green)"""
    while leave(bit):
        bit.move()


if __name__ == '__main__':
    run(Bit.new_bit)
