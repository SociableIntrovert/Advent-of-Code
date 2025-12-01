
with open('../input', 'r') as file:
    lines = [line.split() for line in file]


safe_count = 0

for line in lines:
    increase_flag = False 
    decrease_flag = False
    diff_flag = False
    for index in range(0, len(line)):
        if index == len(line) - 1:
            if (increase_flag and decrease_flag) or diff_flag:
                pass 
            else:
                safe_count += 1
        else:
            if int(line[index]) < int(line[index + 1]):
                increase_flag = True 
            if int(line[index]) > int(line[index + 1]):
                decrease_flag = True 
            if int(line[index]) == int(line[index + 1]):
                increase_flag = True 
                decrease_flag = True 
            if abs(int(line[index]) - int(line[index + 1])) < 1 or abs(int(line[index]) - int(line[index + 1])) > 3:
                diff_flag = True

print(safe_count)

