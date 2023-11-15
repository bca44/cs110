import sys


def get_items(how_many, prompt):
    items = []
    while len(items) < how_many:
        item = input(prompt + ': ')
        items.append(item)
    return items


def display_items(items):
    for item in items:
        print(f'- {item}')
        
        
def main(how_many, prompt):
    items = get_items(how_many, prompt)
    display_items(items)


if __name__ == "__main__":
    how_many = int(sys.argv[1])
    prompt = sys.argv[2]
    main(how_many, prompt)
    
