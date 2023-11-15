def main():
    board = ["", "", "", "", ""]

    while True:
        # displays current board
        print(f"{board}\n")

        # takes user input for slot and pic
        slot = input("Slot: ")
        if slot == "":
            break
        pic = input("Pic: ")

        # puts pic item into board at index 'slot'
        board[int(slot)] = pic


if __name__ == '__main__':
    main()
