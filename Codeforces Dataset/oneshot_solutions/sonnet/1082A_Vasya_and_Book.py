import sys

def solve(n, x, y, d):
    if x == y:
        return 0
    
    options = []
    
    # Direct path
    if abs(y - x) % d == 0:
        options.append(abs(y - x) // d)
    
    # Via page 1
    if (y - 1) % d == 0:
        steps_to_1 = (x - 1 + d - 1) // d  # ceil((x - 1) / d)
        steps_from_1 = (y - 1) // d
        options.append(steps_to_1 + steps_from_1)
    
    # Via page n
    if (n - y) % d == 0:
        steps_to_n = (n - x + d - 1) // d  # ceil((n - x) / d)
        steps_from_n = (n - y) // d
        options.append(steps_to_n + steps_from_n)
    
    return min(options) if options else -1

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    for _ in range(t):
        n = int(data[idx])
        x = int(data[idx + 1])
        y = int(data[idx + 2])
        d = int(data[idx + 3])
        idx += 4
        print(solve(n, x, y, d))

if __name__ == "__main__":
    main()
