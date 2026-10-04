import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases


# --- clause: smallest_sum :: (a: list[int]) -> int ---
def smallest_sum(a):
    answer = 0
    index = 0
    while index < len(a):
        answer |= a[index]
        index += 1
    return answer

# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(str(smallest_sum(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
