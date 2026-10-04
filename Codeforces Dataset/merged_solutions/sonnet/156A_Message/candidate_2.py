import sys


# --- clause: read_input :: () -> tuple[str, str] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    return tokens[0].decode(), tokens[1].decode()


# --- clause: fewest_changes :: (s: str, u: str) -> int ---
def fewest_changes(s, u):
    best = 0
    for begin in range(-len(u), len(s) + 1):
        same = 0
        for i in range(len(u)):
            at = begin + i
            if 0 <= at < len(s) and s[at] == u[i]:
                same += 1
        if same > best:
            best = same
    return len(u) - best


# --- clause: main :: () -> None ---
def main():
    s, u = read_input()
    sys.stdout.write("%d\n" % fewest_changes(s, u))


if __name__ == "__main__":
    main()
