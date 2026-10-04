import sys


# --- clause: read_input :: () -> list[list[tuple[str, str]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        songs = []
        for _ in range(n):
            songs.append((data[pos].decode(), data[pos + 1].decode()))
            pos += 2
        cases.append(songs)
    return cases


# --- clause: link_songs :: (songs: list[tuple[str, str]]) -> list[int] ---
def link_songs(songs):
    n = len(songs)
    links = [0] * n
    for i in range(n):
        for j in range(n):
            if i != j and (songs[i][0] == songs[j][0] or songs[i][1] == songs[j][1]):
                links[i] |= 1 << j
    return links


# --- clause: longest_chain :: (n: int, links: list[int]) -> int ---
def longest_chain(n, links):
    reach = [0] * (1 << n)
    for i in range(n):
        reach[1 << i] = 1 << i
    best = 1 if n else 0
    for mask in range(1, 1 << n):
        ends = reach[mask]
        if not ends:
            continue
        size = bin(mask).count("1")
        if size > best:
            best = size
        for i in range(n):
            if not (ends >> i) & 1:
                continue
            free = links[i] & ~mask
            while free:
                low = free & (-free)
                j = low.bit_length() - 1
                reach[mask | low] |= 1 << j
                free -= low
    return best


# --- clause: main :: () -> None ---
def main():
    out = []
    for songs in read_input():
        n = len(songs)
        out.append(n - longest_chain(n, link_songs(songs)))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
