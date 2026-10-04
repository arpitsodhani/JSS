import sys


# --- clause: read_input :: () -> list[list[tuple[int, int]]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    q = raw[0]
    offset = 1
    cases = []
    for _ in range(q):
        n = raw[offset]
        offset += 1
        boards = [(raw[offset + 2 * i], raw[offset + 2 * i + 1]) for i in range(n)]
        offset += 2 * n
        cases.append(boards)
    return cases


# --- clause: least_rubles :: (boards: list[tuple[int, int]]) -> int ---
def least_rubles(boards):
    big = float("inf")
    best = [0, boards[0][1], 2 * boards[0][1]]
    for i in range(1, len(boards)):
        height, price = boards[i]
        before = boards[i - 1][0]
        step = [big, big, big]
        for add in range(3):
            for prev in range(3):
                if height + add == before + prev:
                    continue
                number = best[prev] + add * price
                if number < step[add]:
                    step[add] = number
        best = step
    return min(best)


# --- clause: main :: () -> None ---
def main():
    out = []
    for boards in read_input():
        out.append(least_rubles(boards))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
