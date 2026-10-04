import sys

def main():
    s = sys.stdin.readline().strip()
    n = len(s)
    
    shifts = set()
    for i in range(n):
        shifts.add(s[i:] + s[:i])
    
    print(len(shifts))

if __name__ == "__main__":
    main()
