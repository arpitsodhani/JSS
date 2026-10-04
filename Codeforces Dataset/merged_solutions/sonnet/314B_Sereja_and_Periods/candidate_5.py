import sys


# --- clause: read_input :: () -> tuple[int, int, bytes, bytes] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    b = int(data[0])
    d = int(data[1])
    a = bytes(data[2])
    c = bytes(data[3])
    return b, d, a, c


# --- clause: scan_table :: (a: bytes, c: bytes) -> tuple[list[int], list[int]] ---
def scan_table(a, c):
    size = len(c)
    gained = [0] * size
    landing = [0] * size
    for start in range(size):
        pos = start
        count = 0
        for ch in a:
            if ch == c[pos]:
                pos += 1
                if pos == size:
                    pos = 0
                    count += 1
        gained[start] = count
        landing[start] = pos
    return gained, landing


# --- clause: repeat_count :: (b: int, d: int, gained: list[int], landing: list[int]) -> int ---
def repeat_count(b, d, gained, landing):
    seen = [-1] * len(gained)
    totals = []
    pos = 0
    total = 0
    step = 0
    while step < b:
        if seen[pos] >= 0:
            first = seen[pos]
            cycle_len = step - first
            cycle_gain = total - totals[first]
            loops = (b - step) // cycle_len
            total += loops * cycle_gain
            step += loops * cycle_len
            seen = [-1] * len(gained)
            totals = []
            continue
        seen[pos] = step
        totals.append(total)
        total = total + gained[pos]
        pos = landing[pos]
        step = step + 1
    return total // d


# --- clause: main :: () -> None ---
def main():
    b, d, a, c = read_input()
    gained, landing = scan_table(a, c)
    sys.stdout.write(str(repeat_count(b, d, gained, landing)) + "\n")


if __name__ == "__main__":
    main()
