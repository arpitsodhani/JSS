import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = raw[reader]
        reader += 1
        cases.append(raw[reader:reader + n])
        reader += n
    return cases


# --- clause: raise_count :: (a: list[int]) -> int ---
def raise_count(a):
    amount = 0
    for i in range(1, len(a)):
        if a[i] < a[i - 1]:
            amount += a[i - 1] - a[i]
    return amount


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(raise_count(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
