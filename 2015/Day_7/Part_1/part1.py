import re

# AND    = a & b   
# LSHIFT = a << b
# RSHIFT = a >> b
# NOT    = ~ a
# OR     = a | b

def and_shift (left_op, right_op):
    return left_op & right_op

def left_shift(left_op, right_op):
    return left_op << right_op

def right_shift(left_op, right_op):
    return left_op >> right_op

def not_shift(op):
    return ~ op 

def or_shift(left_op, right_op):
    return left_op | right_op


values = dict()


and_pattern = r'(.{1,}) AND (.{1,}) -> (.{1,})'
lshift_pattern = r'(.{1,}) LSHIFT (.{1,}) -> (.{1,})'
rshift_pattern = r'(.{1,}) RSHIFT (.{1,}) -> (.{1,})'
not_pattern = r'NOT (.{1,}) -> (.{1,})'
or_pattern = r'(.{1,}) OR (.{1,}) -> (.{1,})'
ass_pattern = r'(.{1,}) -> (.{1,})'

eq_pattern = r'(.+) -> (.+)'


with open('../input', 'r') as input:
    lines = [line.strip() for line in input]

for line in lines:
    result = re.search(eq_pattern, line)
    values[result.group(2)] = dict()
    values[result.group(2)]['eq'] = result.group(1)
    values[result.group(2)]['val'] = None 
    if result.group(1).isnumeric():
        values[result.group(2)]['val'] = int(result.group(1))


found_none = True 

while not found_none:
    for key in values:
        

