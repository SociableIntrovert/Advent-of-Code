import re

test_string = r"abc\d"
pattern = r"\\[a-z\\]"

print(re.sub(pattern, r"\\", test_string))