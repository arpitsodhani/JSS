import sys

# Clause read_input [Confidence: 1.00]
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    albums = list(map(int, data[2:2 + m]))
    return n, m, albums

# Clause choose_counts [Confidence: 0.80]
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

# Clause arrange [Confidence: 1.00]
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

# Clause main [Confidence: 1.00]
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

