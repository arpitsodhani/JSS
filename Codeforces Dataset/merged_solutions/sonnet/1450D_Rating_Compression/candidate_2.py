import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    at = 1
    cases = []
    for _ in range(t):
        n = tokens[at]
        at += 1
        cases.append(tokens[at:at + n])
        at += n
    return cases


# --- clause: happy_widths :: (a: list[int]) -> str ---
def happy_widths(a):
    n = len(a)
    good = ["0"] * (n + 1)
    left = 0
    rest = n - 1
    counts = [0] * (n + 2)
    for value in a:
        counts[value] += 1
    smallest = 1
    for size in range(1, n + 1):
        while smallest <= n and counts[smallest] == 0:
            smallest += 1
        if smallest != size:
            break
        good[n - size + 1] = "1"
        if a[left] == size:
            counts[a[left]] -= 1
            left += 1
        elif a[rest] == size:
            counts[a[rest]] -= 1
            rest -= 1
        else:
            break
    seen = [0] * (n + 2)
    single = True
    for value in a:
        if value > n or seen[value]:
            single = False
            break
        seen[value] = 1
    good[1] = "1" if single else "0"
    return "".join(good[1:])


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(happy_widths(a))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
