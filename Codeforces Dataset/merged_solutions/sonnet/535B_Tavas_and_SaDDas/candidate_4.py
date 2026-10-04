import sys


# --- clause: read_input :: () -> str ---
def read_input():
    return sys.stdin.buffer.read().split()[0].decode()


# --- clause: lucky_index :: (n: str) -> int ---
def lucky_index(n):
    place = 0
    for size in range(1, len(n)):
        place += 1 << size
    step = 1 << (len(n) - 1)
    for ch in n:
        if ch == "7":
            place += step
        step //= 2
    return place + 1


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("%d\n" % lucky_index(read_input()))


if __name__ == "__main__":
    main()
