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


# --- clause: raise_to_powers :: (a: list[int]) -> list[tuple[int, int]] ---
def raise_to_powers(a):
    plan = []
    for index in range(1, len(a) + 1):
        value = a[index - 1]
        power = 1
        while power < value:
            power = power * 2
        plan.append((index, power - value))
    return plan


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        moves = raise_to_powers(a)
        out.append(str(len(moves)))
        for index, add in moves:
            out.append(str(index) + " " + str(add))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
