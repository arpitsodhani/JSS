import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    return tokens[1:1 + tokens[0]]


# --- clause: longest_chain :: (a: list[int]) -> int ---
def longest_chain(a):
    top = a[-1]
    chain = [0] * (top + 1)
    finest = 0
    for value in a:
        here = chain[value] + 1
        if here > finest:
            finest = here
        step = value + value
        while step <= top:
            if here > chain[step]:
                chain[step] = here
            step += value
    return finest


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % longest_chain(read_input()))


if __name__ == "__main__":
    main()
