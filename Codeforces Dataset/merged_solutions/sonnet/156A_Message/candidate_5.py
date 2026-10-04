import sys


# --- clause: read_input :: () -> tuple[str, str] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    return raw[0].decode(), raw[1].decode()


# --- clause: fewest_changes :: (s: str, u: str) -> int ---
def fewest_changes(s, u):
    top = 0
    for head_pos in range(-len(u), len(s) + 1):
        same = 0
        for i in range(0, len(u)):
            at = head_pos + i
            if 0 <= at < len(s) and s[at] == u[i]:
                same += 1
        if same > top:
            top = same
    return len(u) - top


# --- clause: main :: () -> None ---
def main():
    s, u = read_input()
    sys.stdout.write("%d\n" % fewest_changes(s, u))


if __name__ == "__main__":
    main()
