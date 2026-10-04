import sys

MOD = 10 ** 9 + 7

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    
    result = []
    for i in range(1, t + 1):
        n = int(data[i])
        ans = n * (n + 1) * (4 * n - 1) // 6
        result.append(str((ans * 2022) % MOD))
    
    print('\n'.join(result))

if __name__ == "__main__":
    main()
