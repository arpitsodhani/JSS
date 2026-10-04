import sys

def solve_case(n, s):
    if all(c == s[0] for c in s):
        return (n + 2) // 3

    while s[0] == s[-1]:
        s = s[1:] + s[0]

    ans = 0
    cnt = 1
    for i in range(1, n):
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            ans += cnt // 3
            cnt = 1
    ans += cnt // 3
    return ans

def main():
    data = sys.stdin.read().strip().split()
    t = int(data[0])
    out = []
    idx = 1
    for _ in range(t):
        n = int(data[idx])
        s = data[idx + 1]
        idx += 2
        out.append(str(solve_case(n, s)))
    print("\n".join(out))

if __name__ == "__main__":
    main()
