import re

vowel_pattern = r'([aeiou])'
double_pattern = r'(.)\1'
bad_pattern = r'(ab|cd|pq|xy)'
nice_count = 0

with open('../input', 'r') as input:
    lines = [line.strip() for line in input]


for line in lines:
    vowel_match = re.findall(vowel_pattern, line)
    double_match = re.findall(double_pattern, line)
    bad_match = re.findall(bad_pattern, line)

    if (vowel_match and len(vowel_match) >= 3) and double_match and not bad_match:
        nice_count += 1


print(nice_count)



# Three vowels
# double letters
# Does not contain ab, cd, pq, xy