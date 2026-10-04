import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n
    return cases


# --- clause: assign_gifts :: (wishes: list[int]) -> list[int] ---
def assign_gifts(wishes):
    n = len(wishes)
    taken = [False] * (n + 1)
    given = [0] * n
    waiting = []
    for i in range(n):
        want = wishes[i]
        if not taken[want]:
            taken[want] = True
            given[i] = want
        else:
            waiting.append(i)
    spare = []
    for value in range(1, n + 1):
        if not taken[value]:
            spare.append(value)
    for spot in range(len(waiting)):
        given[waiting[spot]] = spare[spot]
    for i in waiting:
        if given[i] != i + 1:
            continue
        other = -1
        for j in waiting:
            if j != i:
                other = j
                break
        if other < 0:
            for j in range(n):
                if j != i and given[j] == wishes[i]:
                    other = j
                    break
        given[i], given[other] = given[other], given[i]
    return given


# --- clause: main :: () -> None ---
def main():
    out = []
    for wishes in read_input():
        given = assign_gifts(wishes)
        happy = 0
        for i in range(len(wishes)):
            if given[i] == wishes[i]:
                happy += 1
        out.append(str(happy))
        out.append(" ".join(map(str, given)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
