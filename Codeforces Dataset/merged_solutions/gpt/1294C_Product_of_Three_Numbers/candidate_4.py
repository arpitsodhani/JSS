# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys
    import math

    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    ans = []

    for n in data[1:1 + t]:
        a = -1
        x = n

        d = 2
        while d * d <= x:
            if x % d == 0:
                a = d
                x //= d
                break
            d += 1

        if a == -1:
            ans.append("NO")
            continue

        b = -1
        d = 2
        while d * d <= x:
            if x % d == 0 and d != a:
                b = d
                x //= d
                break
            d += 1

        c = x

        if b != -1 and c > 1 and c != a and c != b:
            ans.append("YES")
            ans.append(f"{a} {b} {c}")
        else:
            ans.append("NO")

    sys.stdout.write("\n".join(ans))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
