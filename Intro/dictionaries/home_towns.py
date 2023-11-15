if __name__ == '__main__':
    hometowns = {
        'Dallin Oaks': 'Provo, UT',
        'Jeffery Holland': 'St George, UT',
        'Merril Bateman': 'Lehi, UT',
        'Cecil Samuelson': 'Salt Lake City, UT',
        'Kevin Worthen': 'Dragerton, UT',
        'Shane Reese': 'Logan, UT'
    }
    for person in ['Kevin Worthen', 'Henry Eyring', 'Shane Reese', 'Ernest Wilkinson', 'Karl Maeser']:
        if person in hometowns:
            print(f'{person} was born in {hometowns[person]}.')
        else:
            print(f"I don't know where {person} was born.")
