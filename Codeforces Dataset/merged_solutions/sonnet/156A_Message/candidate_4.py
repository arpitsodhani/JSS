import sys


# --- clause: read_input :: () -> tuple[str, str] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    return numbers[0].decode(), numbers[1].decode()


# --- clause: fewest_changes :: (s: str, u: str) -> int ---
def fewest_changes(s, u):
    cost = len(u)
    start = -len(u)
    while start <= len(s):
        wrong = 0
        i = 0
        while i < len(u):
            at = start + i
            if at < 0 or at >= len(s) or s[at] != u[i]:
                wrong += 1
            i += 1
        if wrong < cost:
            cost = wrong
        start += 1
    return cost


# --- clause: main :: () -> None ---
def main():
    s, u = read_input()
    sys.stdout.write("%d\n" % fewest_changes(s, u))


if __name__ == "__main__":
    main()
