from byubit import Bit


def mountain(bit):
    """takes bit down the mountain"""
    """goes until square is blue. when 'on the mountain', right not clear,"""
    """paints green and moves. when 'in air', right clear, moves down"""
    while not bit.is_blue():
        bit.paint("green")
        if not bit.right_clear():
            bit.move()
        else:
            bit.right()
            bit.move()
            bit.left()
    bit.snapshot("mountain")


def river(bit):
    """takes bit across the river"""
    """moves bit til front blocked, gets out of river and onto 'shore'"""
    while bit.front_clear():
        bit.move()
    bit.left()
    bit.move()
    bit.right()
    bit.move()
    bit.snapshot("river")


def cycle(bit):
    """takes bit to the end"""
    """paints red squares, moves, paints last square red when done"""
    while bit.front_clear():
        bit.paint("red")
        bit.move()
    bit.paint("red")
    bit.snapshot("cycle. all done!")


@Bit.worlds('bitathon', 'bitathon2')
def run(bit):
    # optional while loop for multiple obstacles and/or different orders
    # just add while bit.front_clear(): to beginning
    # the while condition will evaluate between functions, and should hold til the end still
    mountain(bit)
    river(bit)
    cycle(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
