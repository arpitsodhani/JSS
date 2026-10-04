import sys


# --- clause: read_input :: () -> tuple[list[int], int, int] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    n = fields[0]
    return fields[1:1 + n], fields[1 + n], fields[2 + n]


# --- clause: best_start :: (people: list[int], s: int, f: int) -> int ---
def best_start(people, s, f):
    n = len(people)
    sums = [0] * (2 * n + 1)
    for i in range(2 * n):
        sums[i + 1] = sums[i] + people[i % n]
    span = f - s
    best = -1
    answer = 1
    for opening in range(1, n + 1):
        first = (s - opening) % n
        total = sums[first + span] - sums[first]
        if total > best:
            best = total
            answer = opening
    return answer


# --- clause: main :: () -> None ---
def main():
    people, s, f = read_input()
    sys.stdout.write("%d\n" % best_start(people, s, f))


if __name__ == "__main__":
    main()
