import sys

def solve(n, x):
    if n == 1:
        return [0]
    elif x == 0:
        # Place all elements except 0, then 0 last
        return list(range(1, n)) + [0]
    elif x >= n:
        # Standard permutation
        return list(range(n))
    else:  # 0 < x < n
        # Place 0..x-1, then x+1..n-1, then x
        return list(range(x)) + list(range(x + 1, n)) + [x]

def main():
    input_data = sys.stdin.read().split()
    idx = 0
    t = int(input_data[idx])
    idx += 1
    for _ in range(t):
        n = int(input_data[idx])
        x = int(input_data[idx + 1])
        idx += 2
        result = solve(n, x)
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    main()
