import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    t = raw[0]
    offset = 1
    cases = []
    for _ in range(t):
        n = raw[offset]
        offset += 1
        cases.append(raw[offset:offset + n])
        offset += n
    return cases


# --- clause: candies_eaten :: (a: list[int]) -> int ---
def candies_eaten(a):
    low = min(a)
    total = 0
    for number in a:
        total += number - low
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(candies_eaten(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
