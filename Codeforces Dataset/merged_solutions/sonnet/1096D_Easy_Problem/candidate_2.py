import sys


# --- clause: read_input :: () -> tuple[int, str, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    s = data[1].decode()
    costs = list(map(int, data[2:2 + n]))
    return n, s, costs


# --- clause: least_ambiguity :: (n: int, s: str, costs: list[int]) -> int ---
def least_ambiguity(n, s, costs):
    word = "hard"
    big = 1 << 62
    state = [0, big, big, big]
    for letter, price in zip(s, costs):
        for slot in (3, 2, 1, 0):
            if state[slot] >= big:
                continue
            if letter != word[slot]:
                continue
            if slot < 3 and state[slot] < state[slot + 1]:
                state[slot + 1] = state[slot]
            state[slot] += price
    return min(state)


# --- clause: main :: () -> None ---
def main():
    n, s, costs = read_input()
    sys.stdout.write(str(least_ambiguity(n, s, costs)) + "\n")


if __name__ == "__main__":
    main()
