import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    t = int(numbers[0])
    cases = []
    for i in range(t):
        cases.append(numbers[2 + 2 * i].decode())
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
    pieces = []
    for s in read_input():
        pieces.append("Alice" if alice_wins(s) else "Bob")
    sys.stdout.write("\n".join(pieces) + "\n")


if __name__ == "__main__":
    main()
