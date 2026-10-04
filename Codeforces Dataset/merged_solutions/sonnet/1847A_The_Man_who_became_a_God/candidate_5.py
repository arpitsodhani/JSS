import sys


# --- clause: read_input :: () -> list[tuple[int, list[int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = raw[offset]
        k = raw[offset + 1]
        offset += 2
        cases.append((k, raw[offset:offset + n]))
        offset += n
    return cases


# --- clause: least_power :: (k: int, a: list[int]) -> int ---
def least_power(k, a):
    gaps = []
    for i in range(1, len(a)):
        step = a[i] - a[i - 1]
        gaps.append(step if step > 0 else -step)
    gaps.sort(reverse=True)
    running = 0
    for spot in range(k - 1, len(gaps)):
        running += gaps[spot]
    return running


# --- clause: main :: () -> None ---
def main():
    out = []
    for k, a in read_input():
        out.append(least_power(k, a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
