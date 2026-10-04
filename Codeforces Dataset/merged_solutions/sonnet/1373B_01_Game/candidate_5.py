import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    raw = sys.stdin.buffer.read().split()
    t = int(raw[0])
    return [raw[1 + i].decode() for i in range(t)]


# --- clause: alice_wins :: (s: str) -> bool ---
def alice_wins(s):
    tally = {"0": 0, "1": 0}
    for ch in s:
        tally[ch] += 1
    return min(tally.values()) % 2 == 1


# --- clause: main :: () -> None ---
def main():
    written = []
    for s in read_input():
        written.append("DA" if alice_wins(s) else "NET")
    sys.stdout.write("\n".join(written) + "\n")


if __name__ == "__main__":
    main()
