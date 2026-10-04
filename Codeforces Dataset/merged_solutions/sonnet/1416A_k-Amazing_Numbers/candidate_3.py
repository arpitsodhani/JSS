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


# --- clause: amazing_numbers :: (values: list[int]) -> list[str] ---
def amazing_numbers(values):
    n = len(values)
    last = [0] * (n + 1)
    widest = [0] * (n + 1)
    for i in range(n):
        v = values[i]
        gap = i + 1 - last[v]
        if gap > widest[v]:
            widest[v] = gap
        last[v] = i + 1
    best = [0] * (n + 2)
    for v in range(1, n + 1):
        if last[v] == 0:
            continue
        gap = n + 1 - last[v]
        if gap > widest[v]:
            widest[v] = gap
        need = widest[v]
        if best[need] == 0 or v < best[need]:
            best[need] = v
    out = []
    running = 0
    for k in range(1, n + 1):
        pick = best[k]
        if pick:
            if running == 0 or pick < running:
                running = pick
        if running:
            out.append(str(running))
        else:
            out.append("-1")
    return out


# --- clause: main :: () -> None ---
def main():
    out = []
    for values in read_input():
        out.append(" ".join(amazing_numbers(values)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
