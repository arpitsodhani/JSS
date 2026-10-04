import sys


# --- clause: read_input :: () -> tuple[int, list[str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    lamps = list(data[1].decode()[:n])
    return n, lamps


# --- clause: recolour :: (n: int, lamps: list[str]) -> int ---
def recolour(n, lamps):
    changed = 0
    for i in range(1, n):
        if lamps[i] != lamps[i - 1]:
            continue
        changed += 1
        left = lamps[i - 1]
        right = lamps[i + 1] if i + 1 < n else ""
        pick = "RGB"
        for colour in pick:
            if colour != left and colour != right:
                lamps[i] = colour
                break
    return changed


# --- clause: main :: () -> None ---
def main():
    n, lamps = read_input()
    changed = recolour(n, lamps)
    garland = "".join(lamps)
    sys.stdout.write(str(changed) + "\n" + garland + "\n")


if __name__ == "__main__":
    main()
