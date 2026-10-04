import sys

def solve(s, t):
    if len(t) == 0:
        return "YES"
    
    j = len(t) - 1
    last_matched = len(s)
    
    for i in range(len(s) - 1, -1, -1):
        if s[i] == t[j]:
            gap = last_matched - i - 1
            if gap % 2 == 0:
                j -= 1
                last_matched = i
                if j < 0:
                    return "YES"
    
    return "NO"

def main():
    input_data = sys.stdin.read().strip().split('\n')
    q = int(input_data[0])
    idx = 1
    for _ in range(q):
        s = input_data[idx]
        t = input_data[idx + 1]
        idx += 2
        print(solve(s, t))

if __name__ == "__main__":
    main()
