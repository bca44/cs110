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


def encode_lines(plain, cipher):
    # uses cipher to encode plaintext
    # works one line at a time, passing each to encode_line
    ciphertext = []
    for line in plain:
        ciphertext.append(encode_line(line, cipher))

    return "".join(ciphertext)


def encode_line(line, cipher):
    # uses cipher to encode 1 line of plaintext
    new_line = ""
    for char in line:
        # if the character keyed in the cipher, replace with cipher value
        if char in cipher:
            char = cipher[char].strip()
        # if lowercase char in cipher, i.e., if char is upper,
        # replace with upper version of cipher value
        elif char.lower() in cipher:
            char = cipher[char.lower()].upper().strip()
        # add char to new line, if modified or not
        new_line += char
    return new_line


def main(codex_file, input_file, output_file):
    # reads in codex
    codex = read_lines(codex_file)
    # converts codex back to dict format
    codex_dict = csv_to_dict(codex)
    # reads in plaintext
    plaintext = read_lines(input_file)
    # encodes plaintext file, using codex file
    ciphertext = encode_lines(plaintext, codex_dict)
    # writes ciphertext to ciphertext_file
    write_lines(ciphertext, output_file)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
