import sys


# --- clause: read_input :: () -> tuple[int, int, int, list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    n = raw[0]
    m = raw[1]
    a = raw[2]
    d = raw[3]
    return n, a, d, sorted(raw[4:4 + m])


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
                start_value = done + 1
                hits = (limit - start_value) // step + 1
                opens += hits
                last = start_value + step * (hits - 1)
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
            start_value = done + 1
            opens += (n - start_value) // step + 1
    return opens


# --- clause: main :: () -> None ---
def main():
    n, a, d, clients = read_input()
    sys.stdout.write("%d\n" % count_openings(n, a, d, clients))


if __name__ == "__main__":
    main()
