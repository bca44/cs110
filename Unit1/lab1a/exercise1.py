from byubit import Bit

@Bit.empty_world(5,3)
def do_stuff(bit):
    bit.paint("blue")
    bit.move()
    bit.move()
    bit.paint("green")
    bit.left()
    bit.move()
    bit.move()
    bit.move()
    bit.paint("red")



if __name__ == "main":
    do_stuff(Bit.new_bit)