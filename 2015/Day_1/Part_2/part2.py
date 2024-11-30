
with open('input1', 'r') as file:
    input = file.read()


floor = 0
position = 0
for character in input:
    position += 1
    if character == '(':
        floor += 1
    else:
        floor -= 1
    if floor < 0:
        break

print(position)