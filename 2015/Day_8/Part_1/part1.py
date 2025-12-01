import re

with open('../input', 'r') as input:
    lines = [line.strip() for line in input]


all_chars = []
actual_chars = []

pattern = r"\\[a-z\\]"

for line in lines:
    all_chars.append(len(line))
    line = line.replace('"', '')
    line = re.sub(pattern, r"\\", line)
    actual_chars.append(len(line))


all_sum = 0
actual_sum = 0

for index in range(0, len(all_chars)):
    all_sum += all_chars[index]
    actual_sum += actual_chars[index]

print(all_sum)
print(actual_sum)
print(all_sum - actual_sum)
