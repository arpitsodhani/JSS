import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    reader = 1
    cases = []
    for _ in range(t):
        n = raw[reader]
        reader += 1
        cases.append(raw[reader:reader + n])
        reader += n
    return cases


# --- clause: alice_wins :: (a: list[int]) -> bool ---
def alice_wins(a):
    tally = {}
    for item in a:
        tally[item] = tally.get(item, 0) + 1
    for item in tally:
        if tally[item] % 2:
            return True
    return False


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append("YES" if alice_wins(a) else "NO")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
