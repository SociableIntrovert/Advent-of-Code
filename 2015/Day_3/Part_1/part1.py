
current_point = [0,0]
visited_points = [[0,0]]

with open('../input', 'r') as input:
    file = input.read()

for character in file:
    if character == '^':
        current_point[1] += 1
        if current_point not in visited_points:
            visited_points.append(current_point[:])
    elif character == 'v':
        current_point[1] -= 1
        if current_point not in visited_points:
            visited_points.append(current_point[:])
    elif character == '<':
        current_point[0] -= 1
        if current_point not in visited_points:
            visited_points.append(current_point[:])
    elif character == '>':
        current_point[0] += 1
        if current_point not in visited_points:
            visited_points.append(current_point[:])


print(len(visited_points))
print(visited_points)

