def convert_direction(curr_pos, instrunction):
    if curr_pos['current_dir'] == 'N':
        if instrunction[0:1] == 'L':
            curr_pos['current_dir'] = 'W'
            curr_pos['x'] -= int(instrunction[1:])
        else:
            curr_pos['current_dir'] = 'E'
            curr_pos['x'] += int(instrunction[1:])
    elif curr_pos['current_dir'] == 'E':
        if instrunction[0:1] == 'L':
            curr_pos['current_dir'] = 'N'
            curr_pos['y'] += int(instrunction[1:])
        else:
            curr_pos['current_dir'] = 'S'
            curr_pos['y'] -= int(instrunction[1:])
    elif curr_pos['current_dir'] == 'S':
        if instrunction[0:1] == 'L':
            curr_pos['current_dir'] = 'E'
            curr_pos['x'] += int(instrunction[1:])
        else:
            curr_pos['current_dir'] = 'W'
            curr_pos['x'] -= int(instrunction[1:])
    elif curr_pos['current_dir'] == 'W':
        if instrunction[0:1] == 'L':
            curr_pos['current_dir'] = 'S'
            curr_pos['y'] -= int(instrunction[1:])
        else:
            curr_pos['current_dir'] = 'N'
            curr_pos['y'] += int(instrunction[1:])

    return curr_pos


directions = []
starting_pos = {
    'x': 0,
    'y': 0,
    'current_dir': 'N'
}

with open('input', 'r') as file:
    text = file.read()
    directions = text.split(',')

    for index, direction in enumerate(directions):
        directions[index] = directions[index].strip()

for direction in directions:
    starting_pos = convert_direction(starting_pos, direction)

print(starting_pos)
    
