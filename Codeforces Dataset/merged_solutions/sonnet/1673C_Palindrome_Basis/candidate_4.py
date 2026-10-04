import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: palindromes_up_to :: (limit: int) -> list[int] ---
def palindromes_up_to(limit):
    out = []
    value = 1
    while value <= limit:
        left = value
        flipped = 0
        while left:
            flipped = flipped * 10 + left % 10
            left //= 10
        if flipped == value:
            out.append(value)
        value += 1
    return out


# --- clause: partition_counts :: (limit: int) -> list[int] ---
def partition_counts(limit):
    mod = 10 ** 9 + 7
    ways = [0 for _ in range(limit + 1)]
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
