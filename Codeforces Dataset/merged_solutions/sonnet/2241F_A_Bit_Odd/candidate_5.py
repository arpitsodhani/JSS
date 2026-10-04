import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    t = int(raw[0])
    cases = []
    for i in range(t):
        cases.append(raw[2 + 2 * i].decode())
    return cases


# --- clause: alice_wins :: (s: str) -> bool ---
def alice_wins(s):
    core = s.lstrip("0").rstrip("1")
    i = 0
    while i < len(core):
        j = i
        while j < len(core) and core[j] == core[i]:
            j += 1
        if (j - i) % 2:
            return True
        i = j
    return False


# --- clause: main :: () -> None ---
def main():
    written = []
    for s in read_input():
        written.append("Alice" if alice_wins(s) else "Bob")
    sys.stdout.write("\n".join(written) + "\n")


if __name__ == "__main__":
    main()
