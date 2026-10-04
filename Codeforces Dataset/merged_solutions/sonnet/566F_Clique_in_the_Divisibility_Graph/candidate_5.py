import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    raw = list(map(int, sys.stdin.buffer.read().split()))
    return raw[1:1 + raw[0]]


# --- clause: longest_chain :: (a: list[int]) -> int ---
def longest_chain(a):
    top = a[-1]
    chain = [0] * (top + 1)
    best = 0
    for item in a:
        here = chain[item] + 1
        if here > best:
            best = here
        advance = item + item
        while advance <= top:
            if here > chain[advance]:
                chain[advance] = here
            advance += item
    return best


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % longest_chain(read_input()))


if __name__ == "__main__":
    main()
