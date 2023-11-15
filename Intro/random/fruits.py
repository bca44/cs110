import random


def apples(size):
    """
    Collect a list of 'apples', but 10% of the time, an item is 'bananas!' instead.
    """
    result = []
    while len(result) < size:
        if random.random() < 0.1:
            result.append('bananas!')
        else:
            result.append('apples')
    return result


if __name__ == '__main__':
    fruits = apples(40)
    print(fruits)
