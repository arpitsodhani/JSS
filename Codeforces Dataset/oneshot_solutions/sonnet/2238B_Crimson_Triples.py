import sys

def solve(n):
    result = 0
    m = 1
    while m <= n:
        q = n // m
        next_m = n // q + 1
        count = min(next_m, n + 1) - m
        result += q * q * count
        m = next_m
    return result

def main():
    data = sys.stdin.buffer.read().decode().split()
    t = int(data[0])
    for i in range(1, t + 1):
        n = int(data[i])
        print(solve(n))

if __name__ == "__main__":
    main()
