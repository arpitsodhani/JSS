import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    fields = sys.stdin.buffer.read().split()
    t = int(fields[0])
    return [fields[1 + i].decode() for i in range(t)]


# --- clause: alice_wins :: (s: str) -> bool ---
def alice_wins(s):
    ones = 0
    for ch in s:
        if ch == "1":
            ones += 1
    zeros = len(s) - ones
    moves = ones if ones < zeros else zeros
    return moves % 2 == 1


# --- clause: main :: () -> None ---
def main():
    collected = []
    for s in read_input():
        collected.append("DA" if alice_wins(s) else "NET")
    sys.stdout.write("\n".join(collected) + "\n")


if __name__ == "__main__":
    main()
