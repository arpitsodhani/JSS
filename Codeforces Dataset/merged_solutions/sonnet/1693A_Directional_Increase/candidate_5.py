import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = raw[reader]
        reader += 1
        cases.append(raw[reader:reader + n])
        reader += n
    return cases


# --- clause: reachable :: (a: list[int]) -> bool ---
def reachable(a):
    running = 0
    done = False
    for item in a:
        running += item
        if running < 0:
            return False
        if done and item != 0:
            return False
        if running == 0:
            done = True
    return running == 0


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append("Yes" if reachable(a) else "No")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
