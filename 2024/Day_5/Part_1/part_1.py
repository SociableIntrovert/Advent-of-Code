

with open('../test_input', 'r') as input:
    lines = [line.strip() for line in input]

orders = dict()
page_sum = 0



end_of_rules = False
for line in lines:
    if '|' in line:
        numbers = line.split('|')
        if numbers[0] in orders:
            orders[numbers[0]]['before'].append(numbers[1])
        else:
            orders[numbers[0]] = dict()
            orders[numbers[0]]['before'] = []
            orders[numbers[0]]['after'] = []
            orders[numbers[0]]['before'].append(numbers[1])


        if numbers[1] in orders:
            orders[numbers[1]]['after'].append(numbers[0])
        else:
            orders[numbers[1]] = dict()
            orders[numbers[1]]['before'] = []
            orders[numbers[1]]['after'] = []
            orders[numbers[1]]['after'].append(numbers[0])

    if ',' in line:
        correct_order = True
        updates = line.split(',')

        for current_index in range(0, len(updates)):
            for after_index in range(current_index + 1, len(updates)):
                # print(f'Is {updates[current_index]} before {updates[after_index]}')
                if updates[after_index] in orders[updates[current_index]]['after']:
                    print(f'{updates[after_index]} can\'t come after {updates[current_index]}')
                    correct_order = False 
                    break
        
        if correct_order:
            print(int(updates[int((len(updates) + 1) / 2)]))
            page_sum += int(updates[int((len(updates) + 1) / 2)])

# print(orders['75'])


# print(orders['before']['87'])
print(page_sum)

        
