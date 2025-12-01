directions = []
starting_pos = {
    'x': 0,
    'y': 0,
    'current_dir': None
}

with open('input', 'r') as file:
    text = file.read()
    directions = text.split(',')

    for index, direction in enumerate(directions):
        directions[index] = directions[index].strip()

for direction in directions:
    
