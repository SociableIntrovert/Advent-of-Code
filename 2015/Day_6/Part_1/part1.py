import re

grid = []

for row in range(0, 1000):
    grid.append([])
    for col in range(0, 1000):
        grid[row].append([])
        grid[row][col] = 0

pattern = r'(.+) (\d+),(\d+) through (\d+),(\d+)'
with open('../input', 'r') as input:
    lines = [line.strip() for line in input]

for line in lines:
    result = re.search(pattern, line)
    action = result.group(1)
    start_x = int(result.group(2))
    start_y = int(result.group(3))
    end_x = int(result.group(4)) + 1
    end_y = int(result.group(5)) + 1

    for x_pos in range(start_x, end_x):
        for y_pos in range(start_y, end_y):
            if action == 'turn on':
                grid[x_pos][y_pos] = 1
            elif action == 'turn off':
                grid[x_pos][y_pos] = 0
            else:
                if grid[x_pos][y_pos] == 0:
                    grid[x_pos][y_pos] = 1
                else:
                    grid[x_pos][y_pos] = 0

on_count = 0
for x_pos in range(0, 1000):
    for y_pos in range(0, 1000):
        if grid[x_pos][y_pos] == 1:
            on_count += 1

print(on_count)




# test_line = "turn off 660,55 through 986,197"

# pattern = r'(.+) (\d+),(\d+) through (\d+),(\d+)'

# result = re.search(pattern, test_line)

# print(result.group(1))
# print(result.group(2))
# print(result.group(3))
# print(result.group(4))
# print(result.group(5))