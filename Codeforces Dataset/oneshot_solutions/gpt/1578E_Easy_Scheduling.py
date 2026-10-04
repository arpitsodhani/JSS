import sys

def solve_case(h, p):
    done_power = 1
    moments = 0

    while moments < h and done_power < p:
        moments += 1
        done_power <<= 1

    remaining = (1 << h) - done_power
    if remaining > 0:
        moments += (remaining + p - 1) // p

    return moments

def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    t = data[0]
    ans = []
    idx = 1
    for _ in range(t):
        h = data[idx]
        p = data[idx + 1]
        idx += 2
        ans.append(str(solve_case(h, p)))

    sys.stdout.write("\n".join(ans))

if __name__ == "__main__":
    main()
