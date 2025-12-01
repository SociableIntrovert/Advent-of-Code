current_pos = 50
landed_on_zero_count = 0

with open('input', 'r') as file:
    turns = file.readlines()

for index, dir in enumerate(turns):
    turns[index] = turns[index].strip()

for turn in turns:
    dir = turn[0:1]
    counter = int(turn[1:])

    if dir == 'L':
        for count in range(0, counter):
            current_pos -= 1
            if current_pos == 0:
                landed_on_zero_count += 1
            elif current_pos == -1:
                current_pos = 99
    elif dir == 'R':
        for count in range(0, counter):
            current_pos += 1
            if current_pos == 100:
                current_pos = 0
                landed_on_zero_count += 1

    # if current_pos == 0:
    #     landed_on_zero_count += 1

print(landed_on_zero_count)
    