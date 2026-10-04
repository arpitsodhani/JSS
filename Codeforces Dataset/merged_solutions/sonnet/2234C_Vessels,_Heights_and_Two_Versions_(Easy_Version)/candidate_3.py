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


# --- clause: volumes :: (h: list[int]) -> list[int] ---
def volumes(h):
    n = len(h)
    answers = []
    forward = [0] * n
    backward = [0] * n
    for empty in range(n):
        best = 0
        for step in range(1, n):
            gate = h[(empty + step - 1) % n]
            if gate > best:
                best = gate
            forward[(empty + step) % n] = best
        best = 0
        for step in range(1, n):
            index = (empty - step) % n
            gate = h[index]
            if gate > best:
                best = gate
            backward[index] = best
        total = 0
        for vessel in range(n):
            if vessel == empty:
                continue
            low = forward[vessel]
            if backward[vessel] < low:
                low = backward[vessel]
            total += low
        answers.append(total)
    return answers


# --- clause: main :: () -> None ---
def main():
    out = []
    for h in read_input():
        out.append(" ".join(map(str, volumes(h))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
