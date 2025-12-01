import hashlib

input = 'iwrupvqb'
end = 0
combined = f'{input}{end}'

while hashlib.md5(combined.encode()).hexdigest()[0:5] != '00000':
    end += 1
    combined = f'{input}{end}'



print(end)