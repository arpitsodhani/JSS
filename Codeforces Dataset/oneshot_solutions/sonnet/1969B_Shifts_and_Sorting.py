import sys

def solve(s):
    ones = 0
    cost = 0
    for c in s:
        if c == '1':
            ones += 1
        else:  # c == '0'
            cost += ones
    return cost

def main():
    data = sys.stdin.buffer.read().decode().strip().split('\n')
    t = int(data[0])
    for i in range(1, t + 1):
        s = data[i].strip()
        print(solve(s))

if __name__ == "__main__":
    main()
