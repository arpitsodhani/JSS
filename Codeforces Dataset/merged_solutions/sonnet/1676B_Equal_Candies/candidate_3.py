import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    t = fields[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = fields[cursor]
        cursor += 1
        cases.append(fields[cursor:cursor + n])
        cursor += n
    return cases


# --- clause: candies_eaten :: (a: list[int]) -> int ---
def candies_eaten(a):
    low = min(a)
    total = 0
    for element in a:
        total += element - low
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(candies_eaten(a))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
