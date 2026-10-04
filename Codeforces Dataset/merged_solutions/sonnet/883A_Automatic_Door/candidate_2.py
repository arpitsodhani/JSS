import sys


# --- clause: read_input :: () -> tuple[int, int, int, list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    m = tokens[1]
    a = tokens[2]
    d = tokens[3]
    return n, a, d, sorted(tokens[4:4 + m])


# --- clause: count_openings :: (n: int, a: int, d: int, clients: list[int]) -> int ---
def count_openings(n, a, d, clients):
    step = d // a + 1
    opens = 0
    shut = -1
    done = 0
    for moment in clients:
        limit = moment // a
        if limit > n:
            limit = n
        if done < limit:
            if a * (done + 1) <= shut:
                absorbed = shut // a
                if absorbed > limit:
                    absorbed = limit
                done = absorbed
            if done < limit:
                first = done + 1
                tally = (limit - first) // step + 1
                opens += tally
                last = first + step * (tally - 1)
                shut = a * last + d
                done = limit
        if moment > shut:
            opens += 1
            shut = moment + d
    if done < n:
        if a * (done + 1) <= shut:
            absorbed = shut // a
            if absorbed > n:
                absorbed = n
            done = absorbed
        if done < n:
            first = done + 1
            opens += (n - first) // step + 1
    return opens


# --- clause: main :: () -> None ---
def main():
    n, a, d, clients = read_input()
    sys.stdout.write("%d\n" % count_openings(n, a, d, clients))


if __name__ == "__main__":
    main()
