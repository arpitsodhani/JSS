import sys


# --- clause: read_input :: () -> tuple[str, str, str] ---
def read_input():
    tokens = sys.stdin.buffer.read().split()
    return tokens[0].decode(), tokens[1].decode(), tokens[2].decode()


# --- clause: match_spots :: (t: str, piece: str) -> list[int] ---
def match_spots(t, piece):
    spots = []
    for i in range(len(t) - len(piece) + 1):
        if t[i:i + len(piece)] == piece:
            spots.append(i)
    return spots


# --- clause: count_distinct :: (t: str, starts: list[int], ends: list[int], shortest: int) -> int ---
def count_distinct(t, starts, ends, shortest):
    mod = (1 << 61) - 1
    base = 131
    n = len(t)
    power = [1] * (n + 1)
    ahead = [0] * (n + 1)
    for i in range(n):
        power[i + 1] = power[i] * base % mod
        ahead[i + 1] = (ahead[i] * base + ord(t[i])) % mod
    seen = set()
    for i in starts:
        for j in ends:
            if j + 1 - i < shortest:
                continue
            span = j + 1 - i
            item = (ahead[j + 1] - ahead[i] * power[span]) % mod
            seen.add((span, item))
    return len(seen)


# --- clause: main :: () -> None ---
def main():
    t, begin, end = read_input()
    starts = match_spots(t, begin)
    ends = [spot + len(end) - 1 for spot in match_spots(t, end)]
    shortest = len(begin) if len(begin) > len(end) else len(end)
    sys.stdout.write("%d\n" % count_distinct(t, starts, ends, shortest))


if __name__ == "__main__":
    main()
