import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    numbers = sys.stdin.buffer.read().split()
    t = int(numbers[0])
    return [numbers[1 + i].decode() for i in range(t)]


# --- clause: kicks_taken :: (s: str, choice: int) -> int ---
def kicks_taken(s, choice):
    goals = [0, 0]
    start = [5, 5]
    bit = 0
    for i in range(10):
        side = i % 2
        if s[i] == "?":
            scored = (choice >> bit) & 1
            bit += 1
        else:
            scored = 1 if s[i] == "1" else 0
        goals[side] += scored
        start[side] -= 1
        if goals[0] > goals[1] + start[1] or goals[1] > goals[0] + start[0]:
            return i + 1
    return 10


# --- clause: fewest_kicks :: (s: str) -> int ---
def fewest_kicks(s):
    best = 10
    for side in (0, 1):
        choice = 0
        bit = 0
        for i in range(10):
            if s[i] != "?":
                continue
            if i % 2 == side:
                choice |= 1 << bit
            bit += 1
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
