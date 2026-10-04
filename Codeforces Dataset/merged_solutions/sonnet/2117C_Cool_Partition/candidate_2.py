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


# --- clause: count_segments :: (a: list[int]) -> int ---
def count_segments(a):
    n = len(a)
    stamp = [0] * (n + 1)
    needed = [False] * (n + 1)
    round_id = 1
    still = 0
    kinds = 0
    distinct = []
    pieces = 0
    for value in a:
        if stamp[value] != round_id:
            stamp[value] = round_id
            distinct.append(value)
            if needed[value]:
                still -= 1
        if still == 0:
            pieces += 1
            for item in distinct:
                if not needed[item]:
                    needed[item] = True
                    kinds += 1
            distinct = []
            round_id += 1
            still = kinds
    return pieces


# --- clause: main :: () -> None ---
def main():
    out = []
    for a in read_input():
        out.append(str(count_segments(a)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
