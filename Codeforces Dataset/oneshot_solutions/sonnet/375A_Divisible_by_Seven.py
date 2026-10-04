import sys
from itertools import permutations

def main():
    s = sys.stdin.readline().strip()
    
    need = {'1': 1, '6': 1, '8': 1, '9': 1}
    rest = []
    zeros = 0
    
    for c in s:
        if c in need and need[c] > 0:
            need[c] -= 1
        elif c == '0':
            zeros += 1
        else:
            rest.append(c)
    
    prefix = ''.join(rest)
    rem = 0
    for c in prefix:
        rem = (rem * 10 + int(c)) % 7
    
    for p in permutations('1689'):
        middle = ''.join(p)
        val = rem
        for c in middle:
            val = (val * 10 + int(c)) % 7
        
        if val == 0:
            print(prefix + middle + '0' * zeros)
            return

if __name__ == "__main__":
    main()
