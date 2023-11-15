import sys


def read_lines(filename):
    """Read lines from a file and return a list of lines."""
    with open(filename) as file:
        return file.readlines()


def write_lines(filename, content):
    """Write a list of lines to a file."""
    with open(filename, "w") as file:
        file.writelines(content)


def get_bins(addresses, zip_to_bin):
    """
    Take a list of addresses and a dictionary to map zip codes to bin numbers.
    Return a list of bin numbers, one per line, in the same order.
    """
    bin_list = []

    for address in addresses:
        # Extract zip code from the last word in the address
        zip_code = int(address.split()[-1])

        # If zip code is documented, add the corresponding bin number
        if zip_code in zip_to_bin:
            bin_list.append(str(zip_to_bin[zip_code]) + "\n")
        # If zip code is not in zip_to_bin, mark it as "unknown"
        else:
            bin_list.append("unknown\n")

    return bin_list


def main(input_file, output_file, zip_to_bin):
    """
    Read addresses from the input file, map zip codes to bin numbers using the dictionary,
    and write the ordered bin numbers to the output file, one per line.
    """
    full_addresses = read_lines(input_file)
    bin_numbers = get_bins(full_addresses, zip_to_bin)
    write_lines(output_file, bin_numbers)


if __name__ == "__main__":
    zip_code_to_delivery_bin = {
        5208: 16,
        10118: 4,
        227: 76,
        12345: 1,
        84604: 25,
        84602: 25,
        20895: 82
    }
    main(sys.argv[1], sys.argv[2], zip_code_to_delivery_bin)
