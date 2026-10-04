import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        cases.append([int(data[pos + i]) for i in range(n)])
        pos += n
    return cases


# --- clause: can_sort :: (values: list[int]) -> str ---
def can_sort(values):
    if values == sorted(values, reverse=True) and len(set(values)) == len(values):
        return "NO"
    return "YES"


# --- clause: main :: () -> None ---
def main():
    out = []
    for case in read_input():
        out.append(can_sort(case))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
