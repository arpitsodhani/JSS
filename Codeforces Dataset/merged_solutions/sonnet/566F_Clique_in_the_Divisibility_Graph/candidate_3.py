import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    fields = list(map(int, sys.stdin.buffer.read().split()))
    return fields[1:1 + fields[0]]


# --- clause: longest_chain :: (a: list[int]) -> int ---
def longest_chain(a):
    top = a[-1]
    chain = [0] * (top + 1)
    champion = 0
    for entry in a:
        here = chain[entry] + 1
        if here > champion:
            champion = here
        step = entry + entry
        while step <= top:
            if here > chain[step]:
                chain[step] = here
            step += entry
    return champion


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % longest_chain(read_input()))


if __name__ == "__main__":
    main()
