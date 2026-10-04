import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    numbers = list(map(int, sys.stdin.buffer.read().split()))
    return numbers[1:1 + numbers[0]]


# --- clause: longest_chain :: (a: list[int]) -> int ---
def longest_chain(a):
    top = a[-1]
    chain = [0 for _ in range(top + 1)]
    peak = 0
    for value in a:
        here = chain[value] + 1
        if here > peak:
            peak = here
        step = value + value
        while step <= top:
            if here > chain[step]:
                chain[step] = here
            step += value
    return peak


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % longest_chain(read_input()))


if __name__ == "__main__":
    main()
