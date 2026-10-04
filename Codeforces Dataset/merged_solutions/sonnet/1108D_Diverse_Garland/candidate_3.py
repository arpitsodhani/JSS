import sys


# --- clause: read_input :: () -> tuple[int, list[str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    lamps = list(str(data[1], "ascii"))
    return n, lamps


# --- clause: recolour :: (n: int, lamps: list[str]) -> int ---
def recolour(n, lamps):
    changed = 0
    i = 1
    while i < n:
        if lamps[i] != lamps[i - 1]:
            i += 1
            continue
        changed += 1
        for colour in "RGB":
            if colour == lamps[i - 1]:
                continue
            if i + 1 < n and colour == lamps[i + 1]:
                continue
            lamps[i] = colour
            break
        i += 1
    return changed


# --- clause: main :: () -> None ---
def main():
    n, lamps = read_input()
    changed = recolour(n, lamps)
    print(changed)
    print("".join(lamps))


if __name__ == "__main__":
    main()
