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
    big = float("inf")
    best = [0, big, big, big]
    for index in range(n):
        letter = s[index]
        price = costs[index]
        for state in range(3, -1, -1):
            if best[state] == big:
                continue
            if letter == word[state]:
                if state == 3:
                    best[3] += price
                else:
                    if best[state] < best[state + 1]:
                        best[state + 1] = best[state]
                    best[state] += price
    return int(min(best))


# --- clause: main :: () -> None ---
def main():
    n, s, costs = read_input()
    sys.stdout.write(str(least_ambiguity(n, s, costs)) + "\n")


if __name__ == "__main__":
    main()
