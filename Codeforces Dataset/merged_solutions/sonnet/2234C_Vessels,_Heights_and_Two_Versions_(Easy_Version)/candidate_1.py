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
        running = 0
        for step in range(1, n):
            running = running if running > h[(empty + step - 1) % n] else h[(empty + step - 1) % n]
            forward[(empty + step) % n] = running
        running = 0
        for step in range(1, n):
            index = (empty - step) % n
            running = running if running > h[index] else h[index]
            backward[index] = running
        total = 0
        for vessel in range(n):
            if vessel == empty:
                continue
            near = forward[vessel]
            far = backward[vessel]
            total += near if near < far else far
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
