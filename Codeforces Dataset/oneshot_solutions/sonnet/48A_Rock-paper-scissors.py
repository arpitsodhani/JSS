s = input().strip()

# Parse the three choices
choices = []
i = 0
while len(choices) < 3:
    if s[i:].startswith('rock'):
        choices.append('rock')
        i += 4
    elif s[i:].startswith('paper'):
        choices.append('paper')
        i += 5
    elif s[i:].startswith('scissors'):
        choices.append('scissors')
        i += 8

f, m, sh = choices

def beats(a, b):
    return (a == 'rock' and b == 'scissors') or \
           (a == 'scissors' and b == 'paper') or \
           (a == 'paper' and b == 'rock')

# Determine winner
if f == m == sh:
    print('?')
elif f == m and f != sh:
    print('S' if beats(sh, f) else '?')
elif f == sh and f != m:
    print('M' if beats(m, f) else '?')
elif m == sh and m != f:
    print('F' if beats(f, m) else '?')
else:
    print('?')
