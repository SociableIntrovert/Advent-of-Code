import re

not_overlapping = r'(..).{0,}\1'
inbetween = r'(.).\1'

# test_string = 'aabcdefgaa'

# overlap_match = re.findall(not_overlapping, test_string)


nice_count = 0

with open('../input', 'r') as input:
    lines = [line.strip() for line in input]


for line in lines:
    not_overlapping_match = re.findall(not_overlapping, line)
    inbetween_match = re.findall(inbetween, line)

    if not_overlapping_match and inbetween_match:
        nice_count += 1


print(nice_count)