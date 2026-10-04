import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = fields[offset]
        offset += 1
        cases.append(fields[offset:offset + n])
        offset += n
    return cases


# --- clause: reachable :: (a: list[int]) -> bool ---
def reachable(a):
    running = 0
    done = False
    for entry in a:
        running += entry
        if running < 0:
            return False
        if done and entry != 0:
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
