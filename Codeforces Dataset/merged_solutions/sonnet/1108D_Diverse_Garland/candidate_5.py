import sys


# --- clause: read_input :: () -> tuple[int, list[str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    lamps = [c for c in data[1].decode()]
    return n, lamps


# --- clause: recolour :: (n: int, lamps: list[str]) -> int ---
def recolour(n, lamps):
    changed = 0
    for i in range(1, n):
        if lamps[i] != lamps[i - 1]:
            continue
        changed += 1
        after = lamps[i + 1] if i + 1 < n else "?"
        for colour in ("R", "G", "B"):
            if colour != lamps[i - 1] and colour != after:
                lamps[i] = colour
                break
    return changed


# --- clause: main :: () -> None ---
def main():
    n, lamps = read_input()
    changed = recolour(n, lamps)
    sys.stdout.write(str(changed) + "\n" + "".join(lamps) + "\n")


if __name__ == "__main__":
    main()
