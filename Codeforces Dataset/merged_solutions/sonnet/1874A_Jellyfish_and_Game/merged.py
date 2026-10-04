import sys

# Clause read_input [Confidence: 1.00]
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
        mine = [int(token) for token in data[pos:pos + n]]
        pos += n
        theirs = [int(token) for token in data[pos:pos + m]]
        pos += m
        cases.append((n, m, k, mine, theirs))
    return cases

# Clause play_round [Confidence: 1.00]
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

# Clause solve_case [Confidence: 0.80]
def solve_case(n, m, k, mine, theirs):
    first = list(mine)
    second = list(theirs)
    play_round(first, second)
    if k == 1:
        return sum(first)
    play_round(second, first)
    if k % 2 == 0:
        return sum(first)
    play_round(first, second)
    return sum(first)

# Clause main [Confidence: 1.00]
def main():
    out = []
    for n, m, k, mine, theirs in read_input():
        out.append(str(solve_case(n, m, k, mine, theirs)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()

