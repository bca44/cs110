def get_blocks():
    """
    user input for which characters to 'block' and what to replace them with
    """
    return input("Characters to block: ").lower(), input("Replacement: ")


def reverse_wordle(block_chars, replacement):
    #
    while True:

        replace_this = input("Word: ")

        if replace_this == "":
            break

        for block_char in block_chars:
            for char in replace_this:

                if char.lower() == block_char:
                    replace_this = replace_this.replace(char, replacement)

        print(replace_this)


def main():
    block_chars, replacement = get_blocks()
    reverse_wordle(block_chars, replacement)



if __name__ == "__main__":
    main()
