import sys


# --- clause: read_input :: () -> tuple[int, int, bytes, bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    b = int(data[0])
    d = int(data[1])
    a = data[2]
    c = data[3]
    return b, d, a, c


# --- clause: scan_table :: (a: bytes, c: bytes) -> tuple[list[int], list[int]] ---
def scan_table(a, c):
    size = len(c)
    gained = []
    landing = []
    for start in range(size):
        pos = start
        count = 0
        for ch in a:
            if ch == c[pos]:
                pos += 1
                if pos == size:
                    pos = 0
                    count += 1
        gained.append(count)
        landing.append(pos)
    return gained, landing


# --- clause: repeat_count :: (b: int, d: int, gained: list[int], landing: list[int]) -> int ---
def repeat_count(b, d, gained, landing):
    pos = 0
    total = 0
    for _ in range(b):
        total += gained[pos]
        pos = landing[pos]
    return total // d


# --- clause: main :: () -> None ---
def main():
    b, d, a, c = read_input()
    gained, landing = scan_table(a, c)
    print(repeat_count(b, d, gained, landing))


if __name__ == "__main__":
    main()
