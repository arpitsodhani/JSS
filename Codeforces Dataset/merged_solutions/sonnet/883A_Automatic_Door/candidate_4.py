import sys


# --- clause: read_input :: () -> tuple[int, int, int, list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    n = numbers[0]
    m = numbers[1]
    a = numbers[2]
    d = numbers[3]
    return n, a, d, sorted(numbers[4:4 + m])


# --- clause: count_openings :: (n: int, a: int, d: int, clients: list[int]) -> int ---
def count_openings(n, a, d, clients):
    step = d // a + 1
    opens = 0
    shut = -1
    done = 0
    queue = list(clients)
    queue.append(None)
    for moment in queue:
        limit = n if moment is None else min(n, moment // a)
        while done < limit:
            first = done + 1
            if a * first <= shut:
                reach = shut // a
                done = limit if reach > limit else reach
                continue
            count = (limit - first) // step + 1
            opens += count
            shut = a * (first + step * (count - 1)) + d
            done = limit
        if moment is not None and moment > shut:
            opens += 1
            shut = moment + d
    return opens


# --- clause: main :: () -> None ---
def main():
    n, a, d, clients = read_input()
    sys.stdout.write("%d\n" % count_openings(n, a, d, clients))


if __name__ == "__main__":
    main()
