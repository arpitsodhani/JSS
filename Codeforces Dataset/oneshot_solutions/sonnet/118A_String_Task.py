s = input()
vowels = 'aoyeui'
result = []
for char in s.lower():
    if char not in vowels:
        result.append('.')
        result.append(char)
print(''.join(result))
