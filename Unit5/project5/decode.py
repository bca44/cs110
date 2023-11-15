import sys


def read_lines(filename):
    with open(filename) as file:
        return file.readlines()


def write_lines(content, filename):
    with open(filename, "w") as file:
        file.writelines(content)


def csv_to_dict(csv_lines):
    # converts csv read_lines output to dict form
    a_dict = {}
    for line in csv_lines:
        key, value = line.split(",")
        a_dict[key] = value

    return a_dict


def invert_cipher(codex):
    # Inverts the codex dictionary
    inverted_codex = {value.strip(): key for key, value in codex.items()}
    return inverted_codex


def decode_lines(ciphertext, codex_dict):
    # decodes ciphertext, using given codex_dict
    plaintext = []
    for line in ciphertext:
        # passes each line of ciphertext to decode_line()
        plaintext.append(decode_line(line, codex_dict))

    return "".join(plaintext)


def decode_line(line, codex_dict):
    # uses codex_dict to decode 1 line of ciphertext
    new_line = ""
    for char in line:
        # if cipher char in codex, replace with plain char
        if char in codex_dict:
            char = codex_dict[char]
            # if lowercase char in codex, replace with upper plain char
        elif char.lower() in codex_dict:
            char = codex_dict[char.lower()].upper()
        # add char to new line, modified or not
        new_line += char
    return new_line


def main(codex_file, input_file, output_file):
    # reads in codex, converts to dict
    codex_lines = read_lines(codex_file)
    codex = csv_to_dict(codex_lines)
    # reverses key value pairs - mapping cipher to plain text
    codex = invert_cipher(codex)

    # reads in input_file (ciphertext)
    ciphertext = read_lines(input_file)

    # decodes ciphertext, using decode_lines
    plaintext = decode_lines(ciphertext, codex)

    # writes plaintext to output_file
    write_lines(plaintext, output_file)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
