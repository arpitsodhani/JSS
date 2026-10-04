import sys


# --- clause: read_input :: () -> tuple[list[int], int, int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    return raw[1:1 + n], raw[1 + n], raw[2 + n]


# --- clause: best_start :: (people: list[int], s: int, f: int) -> int ---
def best_start(people, s, f):
    n = len(people)
    running_sum = [0] * (2 * n + 1)
    for i in range(2 * n):
        running_sum[i + 1] = running_sum[i] + people[i % n]
    span = f - s
    best = -1
    answer = 1
    for head_pos in range(1, n + 1):
        first = (s - head_pos) % n
        total = running_sum[first + span] - running_sum[first]
        if total > best:
            best = total
            answer = head_pos
    return answer


# --- clause: main :: () -> None ---
def main():
    people, s, f = read_input()
    sys.stdout.write("%d\n" % best_start(people, s, f))


if __name__ == "__main__":
    main()
