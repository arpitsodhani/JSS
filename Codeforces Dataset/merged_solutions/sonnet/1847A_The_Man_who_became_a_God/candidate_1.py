import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        k = data[pos + 1]
        pos += 2
        cases.append((k, data[pos:pos + n]))
        pos += n
    return cases


# --- clause: least_power :: (k: int, a: list[int]) -> int ---
def least_power(k, a):
    gaps = []
    for i in range(1, len(a)):
        step = a[i] - a[i - 1]
        gaps.append(step if step > 0 else -step)
    gaps.sort(reverse=True)
    total = 0
    for spot in range(k - 1, len(gaps)):
        total += gaps[spot]
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, a in read_input():
        out.append(least_power(k, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
