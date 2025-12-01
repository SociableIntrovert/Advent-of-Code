
grid = list()
line = 0
with open('../input', 'r') as input:
    lines = [line.strip() for line in input]

for index, line in enumerate(lines):
    grid.append([])
    for letter in line:
        grid[index].append(letter)


# grid = [
#     ['X', '1', '2', '3'],
#     ['M', 'M', '2', '3'],
#     ['A', '1', 'A', '3'],
#     ['S', '1', '2', 'S']
# ]

count = 0
col_end = len(grid) - 1
row_end = len(grid[0]) - 1
# print(col_end)
# print(row_end)

for row in range(0, len(grid)):
    for col in range(0, len(grid[0])):
        # CHECK RIGHT
        if col + 3 > row_end:
            pass 
        else:
            if f'{grid[row][col]}{grid[row][col + 1]}{grid[row][col + 2]}{grid[row][col + 3]}' == 'XMAS':
                count += 1

        # CHECK LEFT
        if col - 3 < 0:
            pass 
        else:
            if f'{grid[row][col]}{grid[row][col - 1]}{grid[row][col - 2]}{grid[row][col - 3]}' == 'XMAS':
                count += 1

        # CHECK UP
        if row - 3 < 0:
            pass 
        else:
            if f'{grid[row][col]}{grid[row - 1][col]}{grid[row - 2][col]}{grid[row - 3][col]}' == 'XMAS':
                count += 1

        # CHECK DOWN
        if row + 3 > col_end:
            pass 
        else:
            if f'{grid[row][col]}{grid[row + 1][col]}{grid[row + 2][col]}{grid[row + 3][col]}' == 'XMAS':
                count += 1

        # CHECK NE
        if row - 3 < 0 or col + 3 > row_end:
            pass 
        else:
            if f'{grid[row][col]}{grid[row - 1][col + 1]}{grid[row - 2][col + 2]}{grid[row - 3][col + 3]}' == 'XMAS':
                count += 1

        # CHECK SE
        if row + 3 > col_end or col + 3 > row_end:
            pass 
        else:
            if f'{grid[row][col]}{grid[row + 1][col + 1]}{grid[row + 2][col + 2]}{grid[row + 3][col + 3]}' == 'XMAS':
                count += 1

        # CHECK SW
        if row + 3 > col_end or col - 3 < 0:
            pass 
        else:
            if f'{grid[row][col]}{grid[row + 1][col - 1]}{grid[row + 2][col - 2]}{grid[row + 3][col - 3]}' == 'XMAS':
                count += 1

        # CHECK NW
        if row - 3 < 0 or col - 3 < 0:
            pass 
        else:
            if f'{grid[row][col]}{grid[row - 1][col - 1]}{grid[row - 2][col - 2]}{grid[row - 3][col - 3]}' == 'XMAS':
                count += 1

print(count)

