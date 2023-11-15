from byubit import Bit


def leave_room(bit):
    """moves bit until it hits a non-empty square"""
    while bit.is_empty():
        bit.move()


def red_line(bit):
    """paints squares red until bit hits a non-empty square"""
    while bit.is_empty():
        bit.paint('red')
        bit.move()


def back_to_room(bit):
    """moves bit until the left side isn't clear"""
    while bit.left_clear():
        bit.move()


@Bit.worlds('red-line')
def draw_line(bit):
    leave_room(bit), bit.snapshot("leave room")
    bit.right()
    bit.move()
    red_line(bit), bit.snapshot("red line")
    bit.right()
    back_to_room(bit), bit.snapshot("back to room")


if __name__ == "__main__":
    draw_line(Bit.new_bit)
