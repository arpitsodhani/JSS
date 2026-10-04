import sys


# --- clause: read_input :: () -> tuple[list[int], int, int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    return tokens[1:1 + n], tokens[1 + n], tokens[2 + n]


# --- clause: best_start :: (people: list[int], s: int, f: int) -> int ---
def best_start(people, s, f):
    n = len(people)
    prefix = [0] * (2 * n + 1)
    for i in range(2 * n):
        prefix[i + 1] = prefix[i] + people[i % n]
    span = f - s
    best = -1
    answer = 1
    for begin in range(1, n + 1):
        first = (s - begin) % n
        total = prefix[first + span] - prefix[first]
        if total > best:
            best = total
            answer = begin
    return answer


# --- clause: main :: () -> None ---
def main():
    people, s, f = read_input()
    sys.stdout.write("%d\n" % best_start(people, s, f))


if __name__ == "__main__":
    main()
