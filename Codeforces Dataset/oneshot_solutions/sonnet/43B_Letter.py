import sys
from collections import Counter

def main():
    lines = sys.stdin.read().splitlines()
    heading = lines[0] if lines else ""
    text = lines[1] if len(lines) > 1 else ""
    
    available = Counter(c for c in heading if c != ' ')
    
    for c in text:
        if c == ' ':
            continue
        if available[c] == 0:
            print("NO")
            return
        available[c] -= 1
    
    print("YES")

main()
