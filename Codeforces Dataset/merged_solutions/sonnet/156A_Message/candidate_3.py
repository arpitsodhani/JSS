import sys


# --- clause: read_input :: () -> tuple[str, str] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    return fields[0].decode(), fields[1].decode()


# --- clause: fewest_changes :: (s: str, u: str) -> int ---
def fewest_changes(s, u):
    finest = 0
    for opening in range(-len(u), len(s) + 1):
        same = 0
        for i in range(len(u)):
            at = opening + i
            if 0 <= at < len(s) and s[at] == u[i]:
                same += 1
        if same > finest:
            finest = same
    return len(u) - finest


# --- clause: main :: () -> None ---
def main():
    s, u = read_input()
    sys.stdout.write("%d\n" % fewest_changes(s, u))


if __name__ == "__main__":
    main()
