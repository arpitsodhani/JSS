import sys


# --- clause: read_input :: () -> list[tuple[int, int, int, list[int], list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        n = int(data[pos])
        m = int(data[pos + 1])
        k = int(data[pos + 2])
        pos += 3
        mine = [int(data[pos + i]) for i in range(n)]
        pos += n
        theirs = [int(token) for token in data[pos:pos + m]]
        pos += m
        cases.append((n, m, k, mine, theirs))
    return cases


# --- clause: play_round :: (mine: list[int], theirs: list[int]) -> None ---
def play_round(mine, theirs):
    worst = 0
    for i in range(1, len(mine)):
        if mine[i] < mine[worst]:
            worst = i
    prize = 0
    for j in range(1, len(theirs)):
        if theirs[j] > theirs[prize]:
            prize = j
    if mine[worst] < theirs[prize]:
        mine[worst], theirs[prize] = theirs[prize], mine[worst]


# --- clause: solve_case :: (n: int, m: int, k: int, mine: list[int], theirs: list[int]) -> int ---
def solve_case(n, m, k, mine, theirs):
    first = mine[:]
    second = theirs[:]
    play_round(first, second)
    if k == 1:
        return sum(first)
    play_round(second, first)
    if k % 2 == 0:
        return sum(first)
    play_round(first, second)
    return sum(first)


# --- clause: main :: () -> None ---
def main():
    out = []
    for case in read_input():
        out.append(str(solve_case(case[0], case[1], case[2], case[3], case[4])))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
