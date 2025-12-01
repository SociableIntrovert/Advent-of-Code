
santa_pos = [0,0]
robo_pos = [0,0]
current_turn = 0
# 0 = Santa
# 1 = Robo Santa
visited_points = [[0,0]]

with open('../input', 'r') as input:
    directions = input.read()

for direction in directions:
    if current_turn == 0:
        current_turn = 1
        if direction == '^':
            santa_pos[1] += 1
            if santa_pos not in visited_points:
                visited_points.append(santa_pos[:])
        elif direction == 'v':
            santa_pos[1] -= 1
            if santa_pos not in visited_points:
                visited_points.append(santa_pos[:])
        elif direction == '<':
            santa_pos[0] -= 1
            if santa_pos not in visited_points:
                visited_points.append(santa_pos[:])
        elif  direction == '>':
            santa_pos[0] += 1
            if santa_pos not in visited_points:
                visited_points.append(santa_pos[:])
    else:
        current_turn = 0
        if direction == '^':
            robo_pos[1] += 1
            if robo_pos not in visited_points:
                visited_points.append(robo_pos[:])
        elif direction == 'v':
            robo_pos[1] -= 1
            if robo_pos not in visited_points:
                visited_points.append(robo_pos[:])
        elif direction == '<':
            robo_pos[0] -= 1
            if robo_pos not in visited_points:
                visited_points.append(robo_pos[:])
        elif  direction == '>':
            robo_pos[0] += 1
            if robo_pos not in visited_points:
                visited_points.append(robo_pos[:])


print(len(visited_points))

