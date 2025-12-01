import re

with open('../input', 'r') as file:
    input = file.read()

# print(input)

pattern = re.compile(r'(mul\(\d+,\d+\))')

mul_pattern = r'mul\((\d+),(\d+)\)'

# test_input = 'mul(1,2)'

# result = re.search(r'.*(mul\(\d+,\d+\)).*', input)

total = 0

for match in pattern.finditer(input):
    # print(match.groups()[0])
    result = re.search(mul_pattern, match.groups()[0])
    # print(result.group(1))
    # print(result.group(2))

    total += int(result.group(1)) * int(result.group(2))

print(total)
    



# print(result.groups())