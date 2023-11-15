import sys


def readlines(filename):
    with open(filename) as file:
        return file.readlines()
    

def writelines(filename, content):
    with open(filename, 'w') as file:
        file.writelines(content)
        
        
def get_state_metrics(lines, state):
    state_metrics = []
    for line in lines:
        tokens = line.split()
        # The state is the first token
        if tokens[0] == state:
            state_metrics.append(tokens)
    return state_metrics


def find_max_unemployment(state_metrics):
    max_ue = None
    for record in state_metrics:
        # % Unemployment is 4th token
        unemployment = float(record[3])
        if max_ue is None or unemployment > max_ue:
            max_ue = unemployment
    return max_ue

        
def main(input_file, state):
    lines = readlines(input_file)
    state_metrics = get_state_metrics(lines, state)
    max_unemp = find_max_unemployment(state_metrics)
    print(f'The max unemployment for {state} between 1976 and 2022 was {max_unemp}')
    
    
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
    
