import sys

def main():
    lines = sys.stdin.read().strip().split('\n')
    n = int(lines[0])
    
    for i in range(1, n + 1):
        word = lines[i]
        c1, c2 = word[0], word[1]
        
        groups_before = (ord(c1) - ord('a')) * 25
        
        if c2 > c1:
            position = ord(c2) - ord('a')
        else:
            position = ord(c2) - ord('a') + 1
        
        print(groups_before + position)

main()
