import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    t = int(tokens[0])
    return [tokens[1 + i].decode() for i in range(t)]


# --- clause: kicks_taken :: (s: str, choice: int) -> int ---
def kicks_taken(s, choice):
    goals = [0, 0]
    low = [5, 5]
    bit = 0
    for i in range(10):
        side = i % 2
        if s[i] == "?":
            scored = (choice >> bit) & 1
            bit += 1
        else:
            scored = 1 if s[i] == "1" else 0
        goals[side] += scored
        low[side] -= 1
        if goals[0] > goals[1] + low[1] or goals[1] > goals[0] + low[0]:
            return i + 1
    return 10


# --- clause: fewest_kicks :: (s: str) -> int ---
def fewest_kicks(s):
    unknown = 0
    for ch in s:
        if ch == "?":
            unknown += 1
    best = 10
    for choice in range(1 << unknown):
        here = kicks_taken(s, choice)
        if here < best:
            best = here
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for s in read_input():
        out.append(fewest_kicks(s))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
