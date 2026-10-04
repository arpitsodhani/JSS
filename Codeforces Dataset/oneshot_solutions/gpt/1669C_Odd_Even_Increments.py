import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    idx = 1
    ans = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        a = data[idx:idx + n]
        idx += n

        ok = True
        odd_parity = a[0] % 2
        even_parity = a[1] % 2 if n > 1 else -1

        for i in range(n):
            if i % 2 == 0:
                if a[i] % 2 != odd_parity:
                    ok = False
                    break
            else:
                if a[i] % 2 != even_parity:
                    ok = False
                    break

        ans.append("YES" if ok else "NO")

    print("\n".join(ans))

if __name__ == "__main__":
    main()
