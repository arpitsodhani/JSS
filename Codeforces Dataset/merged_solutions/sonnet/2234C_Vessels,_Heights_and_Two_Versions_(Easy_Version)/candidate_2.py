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
    for empty in range(n):
        forward = [0] * n
        backward = [0] * n
        running = 0
        index = empty
        for _ in range(n - 1):
            gate = h[index]
            if gate > running:
                running = gate
            index = (index + 1) % n
            forward[index] = running
        running = 0
        index = empty
        for _ in range(n - 1):
            index = (index - 1) % n
            gate = h[index]
            if gate > running:
                running = gate
            backward[index] = running
        total = 0
        for vessel in range(n):
            if vessel != empty:
                total += min(forward[vessel], backward[vessel])
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
