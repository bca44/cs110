from byubit import Bit


def pass_red(bit):
    bit.move()
    while bit:
        if bit.is_red():
            bit.move(), bit.move()
        else:
            bit.snapshot("pass red")
            break


def green_switch(bit):
    if bit.is_green():
        bit.move(), bit.move()
        bit.snapshot("green switch")


def red_to_blue(bit):
    while bit.front_clear():
        bit.paint('blue')
        bit.move(), bit.move()
    bit.paint("blue"), bit.snapshot("red to blue")


@Bit.worlds('fix-reds')
def run(bit):
    pass_red(bit)
    green_switch(bit)
    red_to_blue(bit)


if __name__ == '__main__':
    run(Bit.new_bit)
