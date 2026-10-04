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


# --- clause: best_score :: (a: list[int]) -> int ---
def best_score(a):
    tail = 0
    for i in range(2, len(a)):
        if a[i] > 0:
            tail += a[i]
    first = a[0]
    pair = first + a[1] if len(a) > 1 else first
    front = 0
    if first > front:
        front = first
    if pair > front:
        front = pair
    return tail + front


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(str(best_score(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
