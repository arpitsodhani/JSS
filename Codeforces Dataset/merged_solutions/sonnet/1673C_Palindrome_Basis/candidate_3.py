import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    return fields[1:1 + fields[0]]


# --- clause: palindromes_up_to :: (limit: int) -> list[int] ---
def palindromes_up_to(limit):
    collected = []
    for entry in range(1, limit + 1):
        text = str(entry)
        if text == text[::-1]:
            collected.append(entry)
    return collected


# --- clause: partition_counts :: (limit: int) -> list[int] ---
def partition_counts(limit):
    mod = 10 ** 9 + 7
    ways = [0] * (limit + 1)
    ways[0] = 1
    for entry in palindromes_up_to(limit):
        for total in range(entry, limit + 1):
            ways[total] = (ways[total] + ways[total - entry]) % mod
    return ways


# --- clause: main :: () -> None ---
def main():
    cases = read_input()
    ways = partition_counts(max(cases))
    sys.stdout.write("\n".join(str(ways[n]) for n in cases) + "\n")


if __name__ == "__main__":
    main()
