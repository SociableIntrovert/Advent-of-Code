
with open('../input', 'r') as file:
    lines = [line.strip() for line in file]

left_list = []
right_list = []
id_counts = dict()
total = 0

for line in lines:
    # print(line)
    line_split = line.split('   ')
    left_list.append(int(line_split[0]))
    right_list.append(int(line_split[1]))

left_list.sort()
right_list.sort()

for id in right_list:
    if id in id_counts:
        id_counts[id] += 1
    else:
        id_counts[id] = 1

for id in left_list:
    if id in id_counts:
        total += id * id_counts[id]
        

print(total)

