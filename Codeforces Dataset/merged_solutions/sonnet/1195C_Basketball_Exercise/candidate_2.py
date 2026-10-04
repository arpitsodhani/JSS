import sys


# --- clause: read_input :: () -> tuple[list[int], list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    n = tokens[0]
    return tokens[1:1 + n], tokens[1 + n:1 + 2 * n]


# --- clause: best_team :: (top: list[int], low: list[int]) -> int ---
def best_team(top, low):
    took_top = 0
    took_low = 0
    took_none = 0
    for i in range(len(top)):
        best_other = took_low if took_low > took_none else took_none
        fresh_top = best_other + top[i]
        best_other = took_top if took_top > took_none else took_none
        fresh_low = best_other + low[i]
        fresh_none = took_none
        if took_top > fresh_none:
            fresh_none = took_top
        if took_low > fresh_none:
            fresh_none = took_low
        took_top = fresh_top
        took_low = fresh_low
        took_none = fresh_none
    finest = took_top
    if took_low > finest:
        finest = took_low
    if took_none > finest:
        finest = took_none
    return finest


# --- clause: main :: () -> None ---
def main():
    top, low = read_input()
    sys.stdout.write("%d\n" % best_team(top, low))


if __name__ == "__main__":
    main()
