import sys


# --- clause: read_input :: () -> tuple[int, int, int, list[int]] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    barrels = raw[0]
    per = raw[1]
    slack = raw[2]
    planks = sorted(raw[3:3 + barrels * per])
    return barrels, per, slack, planks


# --- clause: count_usable :: (staves: list[int], l: int) -> int ---
def count_usable(staves, l):
    cap = staves[0] + l
    usable = 0
    for plank in staves:
        if plank <= cap:
            usable += 1
        else:
            break
    return usable


# --- clause: compute_answer :: (n: int, k: int, staves: list[int], usable: int) -> int ---
def compute_answer(n, k, staves, usable):
    if usable < n:
        return 0
    result = 0
    head = 0
    for made in range(n):
        result += staves[head]
        pending = n - made - 1
        head += min(k, usable - head - pending)
    return result


# --- clause: main :: () -> None ---
def main():
    barrels, per, slack, planks = read_input()
    usable = count_usable(planks, slack)
    result = compute_answer(barrels, per, planks, usable)
    sys.stdout.write("%d\n" % result)


if __name__ == "__main__":
    main()
