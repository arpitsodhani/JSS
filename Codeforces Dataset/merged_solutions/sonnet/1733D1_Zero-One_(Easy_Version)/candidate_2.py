import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, bytes, bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    idx = 1
    total = int(data[0])
    cases = []
    for _ in range(total):
        n, x, y = int(data[idx]), int(data[idx + 1]), int(data[idx + 2])
        idx += 3
        first = data[idx]
        second = data[idx + 1]
        idx += 2
        cases.append((n, x, y, first, second))
    return cases


# --- clause: solve_case :: (n: int, x: int, y: int, a: bytes, b: bytes) -> int ---
def solve_case(n, x, y, a, b):
    spots = [i for i in range(n) if a[i] != b[i]]
    count = len(spots)
    if count & 1:
        return -1
    if count == 0:
        return 0
    if count == 2 and spots[0] + 1 == spots[1]:
        return min(x, y + y)
    return y * (count // 2)


# --- clause: main :: () -> None ---
def main():
    answers = []
    for n, x, y, a, b in read_input():
        answers.append(str(solve_case(n, x, y, a, b)))
    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
