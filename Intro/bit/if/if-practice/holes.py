from byubit import Bit


@Bit.worlds('holes')
def run(bit):
    """fixes the pipe"""
    bit.paint('blue')
    while bit.front_clear():
        bit.move()
        if bit.right_clear():
            bit.paint('red')
        elif bit.left_clear():
            bit.paint('green')
        else:
            bit.paint('blue')


if __name__ == '__main__':
    run(Bit.new_bit)
