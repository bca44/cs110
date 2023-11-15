def change_excuse(proverb):
    """
    Change: A bad excuse is better than none.
    To: Every good excuse is worth millions.
    """
    proverb = proverb.replace('A', 'Every')
    proverb = proverb.replace('bad', 'good')
    proverb = proverb.replace('better than', 'worth')
    proverb = proverb.replace('none', 'millions')
    return proverb


def change_mountain(proverb):
    """
    Changes: Do not make a mountain out of a mole hill.
    To: You should make a lemonade out of those lemons!
    """

    proverb = proverb.replace("Do", "You")
    proverb = proverb.replace("not", "should")
    proverb = proverb.replace("mountain", "lemonade")
    proverb = proverb.replace("mole", "lemons.")
    proverb = proverb.replace("hill.", "")

    # problem words: only second a needs to be changed. workaround: change both "a" to "those"
    # after, second .replace() changes only the first "those" to "a"
    # this could be avoided if you could make .replace() work backwards and only replace 1. will research
    proverb = proverb.replace("a ", "those ")
    proverb = proverb.replace("those", "a", 1)

    return proverb


def change_fire(proverb):
    """
    Change: Fight fire with fire.
    To: Fight Thanos with a lightsaber.
    """
    # Write code here

    proverb = proverb.replace("fire ", "Thanos ")
    proverb = proverb.replace("fire.", "a lightsaber.")

    return proverb


def change_late(proverb):
    """
    Change: Better late than never.
    To: Always late and never sorry!
    """
    # Write code here

    proverb = proverb.replace("Better", "Always")
    proverb = proverb.replace("than", "and")
    proverb = proverb.replace("never.", "never sorry!")

    return proverb


def change_your_own(proverb):
    # changes "A penny saved is a penny earned."
    # to "A penny spent is a penny learned."

    proverb = proverb.replace("saved", "spent")
    proverb = proverb.replace("earned", "learned")

    return proverb


def main():
    print(change_excuse('A bad excuse is better than none.'))
    print(change_mountain('Do not make a mountain out of a mole hill.'))
    print(change_fire('Fight fire with fire.'))
    print(change_late('Better late than never.'))
    # Find proverbs here:
    # https://en.wikipedia.org/wiki/List_of_proverbial_phrases
    print(change_your_own('A penny saved is a penny earned.'))


if __name__ == '__main__':
    main()
