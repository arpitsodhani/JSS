import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[1:1 + tokens[0]]


# --- clause: palindromes_up_to :: (limit: int) -> list[int] ---
def palindromes_up_to(limit):
    lines = []
    for value in range(1, limit + 1):
        text = str(value)
        if text == text[::-1]:
            lines.append(value)
    return lines


# --- clause: partition_counts :: (limit: int) -> list[int] ---
def partition_counts(limit):
    mod = 10 ** 9 + 7
    ways = [0] * (limit + 1)
    ways[0] = 1
    for value in palindromes_up_to(limit):
        for total in range(value, limit + 1):
            ways[total] = (ways[total] + ways[total - value]) % mod
    return ways


# --- clause: main :: () -> None ---
def main():
    cases = read_input()
    ways = partition_counts(max(cases))
    sys.stdout.write("\n".join(str(ways[n]) for n in cases) + "\n")


if __name__ == "__main__":
    main()
