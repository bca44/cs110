import sys


def make_pies(pie1, pie2, pie3):
    print("Now making pies...")
    print("...")
    print("OK, we have your pies:")
    print(f"- {pie1}")
    print(f"- {pie2}")
    print(f"- {pie3}")
    print()
    print("Happy Pi Day!")


if __name__ == '__main__':
    if len(sys.argv) <= 3:
        print("This program takes three arguments:")
        print("- name of pie #1")
        print("- name of pie #2")
        print("- name of pie #3")
        exit()

    pie1 = sys.argv[1]
    pie2 = sys.argv[2]
    pie3 = sys.argv[3]
    make_pies(pie1, pie2, pie3)
