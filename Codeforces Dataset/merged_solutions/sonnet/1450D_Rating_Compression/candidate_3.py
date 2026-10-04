import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = fields[offset]
        offset += 1
        cases.append(fields[offset:offset + n])
        offset += n
    return cases


# --- clause: happy_widths :: (a: list[int]) -> str ---
def happy_widths(a):
    n = len(a)
    good = ["0"] * (n + 1)
    left = 0
    rest = n - 1
    buckets = [0] * (n + 2)
    for value in a:
        buckets[value] += 1
    smallest = 1
    for size in range(1, n + 1):
        while smallest <= n and buckets[smallest] == 0:
            smallest += 1
        if smallest != size:
            break
        good[n - size + 1] = "1"
        if a[left] == size:
            buckets[a[left]] -= 1
            left += 1
        elif a[rest] == size:
            buckets[a[rest]] -= 1
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
