import re

values = dict()

values['a'] = 5
values['b'] = 5
values['c'] = values['d'] + values['e']
values['d'] = 1
values['e'] = 1


print(values['c'])

# test_string = 'ea AND eb -> ed'

# and_pattern = r'(.{1,}) AND (.{1,}) -> (.{1,})'

# result = re.search(and_pattern, test_string)

# if result:
#     print(result.group(1))