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
        pos = pos + 1
        cases.append([int(token) for token in data[pos:pos + n]])
        pos += n
    return cases


# --- clause: can_sort :: (values: list[int]) -> str ---
def can_sort(values):
    for i in range(1, len(values)):
        if values[i] >= values[i - 1]:
            return "YES"
    return "NO"


# --- clause: main :: () -> None ---
def main():
    out = []
    for values in read_input():
        out.append(can_sort(values))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
