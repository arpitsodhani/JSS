import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        x = data[pos + 1]
        pos += 2
        cases.append((n, x, data[pos:pos + n]))
        pos += n
    return cases


# --- clause: best_by_length :: (n: int, a: list[int]) -> list[int] ---
def best_by_length(n, a):
    prefix = [0]
    running = 0
    for value in a:
        running += value
        prefix.append(running)
    best = [0] * (n + 1)
    for length in range(1, n + 1):
        best[length] = max(prefix[start + length] - prefix[start]
                           for start in range(n - length + 1))
    return best


# --- clause: answers :: (n: int, x: int, a: list[int]) -> list[int] ---
def answers(n, x, a):
    best = best_by_length(n, a)
    out = []
    for k in range(n + 1):
        top = 0
        for length in range(1, n + 1):
            add = length if length < k else k
            here = best[length] + add * x
            if here > top:
                top = here
        out.append(top)
    return out


# --- clause: main :: () -> None ---
def main():
    lines = []
    for n, x, a in read_input():
        lines.append(" ".join(map(str, answers(n, x, a))))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
