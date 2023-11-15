import sys
import random


def write_lines(content, filename):
    with open(filename, "w") as file:
        file.writelines(content)


def make_codex():
    # generates randomized simple substitution cipher
    # key = original letter, value = ciphered replacement
    codex = {}
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for key, value in zip(alphabet, random.sample(alphabet, len(alphabet))):
        codex[key] = value

    return codex


def make_csv(a_dict):
    # puts dict into csv format
    # each line {key, value}
    csv = []
    for key, value in a_dict.items():
        csv.append(f"{key},{value[0]}\n")

    return csv


def main(output_file):
    # generates a randomized simple substitution cipher
    codex = make_codex()
    # puts dict in CSV format
    csv_codex = make_csv(codex)
    # write codex to output CSV file
    write_lines(csv_codex, output_file)


if __name__ == "__main__":
    main(sys.argv[1])
