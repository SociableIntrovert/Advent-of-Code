import hashlib

input = 'iwrupvqb'
end = 0
combined = f'{input}{end}'

while hashlib.md5(combined.encode()).hexdigest()[0:6] != '000000':
    end += 1
    combined = f'{input}{end}'



print(end)