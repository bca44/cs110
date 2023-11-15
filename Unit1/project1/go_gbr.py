from byubit import Bit


def get_to_green(bit):
    """ paint green until green square; turn right on green square"""
    while not bit.is_green():
        bit.paint('green')
        bit.move()
    while bit.is_green():
        bit.snapshot("made it to green")
        bit.right()
        bit.move()


def get_to_blue(bit):
    """ paint blue until blue square; turn left on blue square"""
    while not bit.is_blue():
        bit.paint('blue')
        bit.move()
    while bit.is_blue():
        bit.snapshot("made it to blue")
        bit.left()
        bit.move()


def get_to_red(bit):
    """ paint red until red square; stop when bit.is_red()"""
    while not bit.is_red():
        bit.paint('red')
        bit.move()


@Bit.worlds("go-go-go", "og-og-og")
def go_gbr(bit):
    get_to_green(bit), bit.snapshot("starting blue")
    get_to_blue(bit), bit.snapshot("starting red")
    get_to_red(bit), bit.snapshot("made it to red. all done!")


if __name__ == '__main__':
    go_gbr(Bit.new_bit)
