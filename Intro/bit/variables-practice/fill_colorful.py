from byubit import Bit


def fill_same_(bit):
    """fills a column with the color passed to it"""
    """returns to starting spot and orientation"""
    color = bit.get_color()
    bit.left()
    while bit.front_clear():
        bit.move()
        bit.paint(color)
    bit.left(), bit.left()
    while bit.front_clear():
        bit.move()
    bit.left()
    bit.snapshot("filled column")


@Bit.worlds('colors')
def fill_colorful(bit):
    while bit.front_clear():
        (bit)
        bit.move()
    (bit)
    bit.snapshot("all done")
        
        
if __name__ == '__main__':
    fill_colorful(Bit.new_bit)
