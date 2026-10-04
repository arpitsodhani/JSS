import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    while len(cases) < t:
        n = int(data[pos])
        pos += 1
        cases.append([int(token) for token in data[pos:pos + n]])
        pos += n
    return cases


# --- clause: can_sort :: (values: list[int]) -> str ---
def can_sort(values):
    ordered = True
    for a, b in zip(values, values[1:]):
        if a <= b:
            ordered = False
            break
    if ordered:
        return "NO"
    return "YES"


# --- clause: main :: () -> None ---
def main():
    out = []
    for values in read_input():
        out.append(can_sort(values))
    print("\n".join(out))


if __name__ == "__main__":
    main()
