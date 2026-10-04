import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = tokens[pos]
        pos += 1
        cases.append(tokens[pos:pos + n])
        pos += n
    return cases


# --- clause: candies_eaten :: (a: list[int]) -> int ---
def candies_eaten(a):
    low = min(a)
    total = 0
    for item in a:
        total += item - low
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(candies_eaten(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
