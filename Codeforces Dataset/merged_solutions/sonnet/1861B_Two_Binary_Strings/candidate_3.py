import sys


# --- clause: read_input :: () -> list[tuple[str, str]] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    t = int(fields[0])
    cases = []
    for i in range(t):
        cases.append((fields[1 + 2 * i].decode(), fields[2 + 2 * i].decode()))
    return cases


# --- clause: can_match :: (a: str, b: str) -> bool ---
def can_match(a, b):
    for i in range(len(a) - 1):
        if a[i] == "0" and b[i] == "0" and a[i + 1] == "1" and b[i + 1] == "1":
            return True
    return False


# --- clause: main :: () -> None ---
def main():
    collected = []
    for a, b in read_input():
        collected.append("YES" if can_match(a, b) else "NO")
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()
