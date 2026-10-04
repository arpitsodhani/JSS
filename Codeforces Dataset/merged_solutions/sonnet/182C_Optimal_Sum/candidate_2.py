import sys


# --- clause: read_input :: () -> tuple[int, int, list[int], int] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    length = data[1]
    a = data[2:2 + n]
    k = data[2 + n]
    return n, length, a, k


# --- clause: best_after_flips :: (n: int, length: int, a: list[int], k: int) -> int ---
def best_after_flips(n, length, a, k):
    negatives = sorted(set(-v for v in a if v < 0))
    size = len(negatives)
    rank = {}
    for index in range(size):
        rank[negatives[index]] = index + 1
    counts = [0] * (size + 1)
    sums = [0] * (size + 1)
    top = 1
    while top * 2 <= size:
        top *= 2
    running = 0
    below = 0
    below_sum = 0
    answer = None
    for i in range(n):
        value = a[i]
        running += value
        if value < 0:
            below += 1
            below_sum -= value
            spot = rank[-value]
            while spot <= size:
                counts[spot] += 1
                sums[spot] -= value
                spot += spot & -spot
        if i >= length:
            gone = a[i - length]
            running -= gone
            if gone < 0:
                below -= 1
                below_sum += gone
                spot = rank[-gone]
                while spot <= size:
                    counts[spot] -= 1
                    sums[spot] += gone
                    spot += spot & -spot
        if i + 1 >= length:
            skip = below - k
            if skip < 0:
                skip = 0
            dropped = 0
            need = skip
            spot = 0
            step = top
            while step:
                nxt = spot + step
                if nxt <= size and counts[nxt] <= need:
                    need -= counts[nxt]
                    dropped += sums[nxt]
                    spot = nxt
                step >>= 1
            if need:
                dropped += need * negatives[spot]
            here = running + 2 * (below_sum - dropped)
            if answer is None or here > answer:
                answer = here
    return answer


# --- clause: main :: () -> None ---
def main():
    n, length, a, k = read_input()
    first = best_after_flips(n, length, a, k)
    second = best_after_flips(n, length, [-v for v in a], k)
    sys.stdout.write(str(first if first > second else second) + "\n")


if __name__ == "__main__":
    main()
