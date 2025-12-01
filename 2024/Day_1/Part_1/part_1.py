
with open('../input', 'r') as file:
    lines = [line.strip() for line in file]

left_list = []
right_list = []
total_distance = 0

for line in lines:
    # print(line)
    line_split = line.split('   ')
    left_list.append(int(line_split[0]))
    right_list.append(int(line_split[1]))

left_list.sort()
right_list.sort()

for position in range(0, len(left_list)):
    total_distance += abs(right_list[position] - left_list[position])

print(total_distance)