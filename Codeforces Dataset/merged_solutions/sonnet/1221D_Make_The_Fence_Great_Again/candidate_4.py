import sys


# --- clause: read_input :: () -> list[list[tuple[int, int]]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    q = numbers[0]
    reader = 1
    cases = []
    for _ in range(q):
        n = numbers[reader]
        reader += 1
        boards = [(numbers[reader + 2 * i], numbers[reader + 2 * i + 1]) for i in range(n)]
        reader += 2 * n
        cases.append(boards)
    return cases


# --- clause: least_rubles :: (boards: list[tuple[int, int]]) -> int ---
def least_rubles(boards):
    big = float("inf")
    best = []
    for add in range(3):
        best.append(add * boards[0][1])
    i = 1
    while i < len(boards):
        height, price = boards[i]
        before = boards[i - 1][0]
        step = []
        for add in range(3):
            cheapest = big
            prev = 0
            while prev < 3:
                if height + add != before + prev and best[prev] + add * price < cheapest:
                    cheapest = best[prev] + add * price
                prev += 1
            step.append(cheapest)
        best = step
        i += 1
    return min(best)


# --- clause: main :: () -> None ---
def main():
    out = []
    for boards in read_input():
        out.append(least_rubles(boards))
    sys.stdout.write("\n".join(map(str, out)) + "\n")


if __name__ == "__main__":
    main()
