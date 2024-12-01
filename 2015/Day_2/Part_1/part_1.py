

    

with open('../input', 'r') as file:
    gifts = [line.strip() for line in file]

total_paper = 0

# 0 = length
# 1 = width
# 2 = height

# 2 * 0 * 1
# 2 * 1 * 2
# 2 * 2 * 0

for gift in gifts:
    values = gift.split('x')
    values[0] = int(values[0])
    values[1] = int(values[1])
    values[2] = int(values[2])
    # print(values)
    total_paper += (2 * (values[0] * values[1])) + (2 * (values[1] * values[2])) + (2 * (values[2] * values[0])) + (min([values[0] * values[1], values[1] * values[2], values[2] * values[0]]))


print(total_paper)
