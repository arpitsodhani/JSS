import sys


# --- clause: read_input :: () -> tuple[int, int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    albums = [int(token) for token in data[2:m + 2]]
    return n, m, albums


# --- clause: choose_counts :: (n: int, m: int, albums: list[int]) -> list[int] | None ---
def choose_counts(n, m, albums):
    half = n // 2
    take = []
    for size in albums:
        if size > half:
            take.append(half)
        else:
            take.append(size)
    if sum(take) < n:
        return None
    excess = sum(take) - n
    for i in range(m):
        if excess == 0:
            break
        drop = take[i]
        if drop > excess:
            drop = excess
        take[i] -= drop
        excess -= drop
    return take


# --- clause: arrange :: (n: int, m: int, take: list[int]) -> list[int] ---
def arrange(n, m, take):
    order = sorted(range(m), key=lambda i: -take[i])
    gallery = [0] * n
    slot = 0
    for i in order:
        for _ in range(take[i]):
            gallery[slot] = i + 1
            slot += 2
            if slot >= n:
                slot = 1
    return gallery


# --- clause: main :: () -> None ---
def main():
    n, m, albums = read_input()
    take = choose_counts(n, m, albums)
    if take is None:
        sys.stdout.write("-1\n")
        return
    gallery = arrange(n, m, take)
    sys.stdout.write(" ".join(map(str, gallery)) + "\n")


if __name__ == "__main__":
    main()
