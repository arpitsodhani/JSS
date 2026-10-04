import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    t = numbers[0]
    cursor = 1
    cases = []
    for _ in range(t):
        n = numbers[cursor]
        cursor += 1
        cases.append(numbers[cursor:cursor + n])
        cursor += n
    return cases


# --- clause: assign_gifts :: (wishes: list[int]) -> list[int] ---
def assign_gifts(wishes):
    n = len(wishes)
    holder = [0] * (n + 1)
    given = [0] * n
    for i in range(n - 1, -1, -1):
        holder[wishes[i]] = i + 1
    waiting = []
    spare = []
    for value in range(1, n + 1):
        owner = holder[value]
        if owner:
            given[owner - 1] = value
        else:
            spare.append(value)
    for i in range(n):
        if given[i] == 0:
            waiting.append(i)
    for spot in range(len(waiting)):
        given[waiting[spot]] = spare[spot]
    spot = 0
    while spot < len(waiting):
        i = waiting[spot]
        if given[i] == i + 1:
            other = waiting[0] if spot else (waiting[1] if len(waiting) > 1 else -1)
            if other < 0:
                for j in range(n):
                    if j != i and given[j] == wishes[i]:
                        other = j
                        break
            given[i], given[other] = given[other], given[i]
        spot += 1
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
