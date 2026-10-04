import sys

def main():
    n = sys.stdin.read().strip()
    
    length = len(n)
    result = (1 << length) - 2
    
    value = 0
    for c in n:
        value *= 2
        if c == '7':
            value += 1
    
    print(result + value + 1)

if __name__ == "__main__":
    main()
