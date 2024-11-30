
with open('input1', 'r') as file:
    input = file.read()


floor = 0
for character in input:
    if character == '(':
        floor += 1
    else:
        floor -= 1

print(floor)
