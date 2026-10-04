import sys


# --- clause: read_input :: () -> tuple[int, list[str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    lamps = [chr(byte) for byte in data[1]]
    return n, lamps


# --- clause: recolour :: (n: int, lamps: list[str]) -> int ---
def recolour(n, lamps):
    changed = 0
    for i in range(1, n):
        if lamps[i] != lamps[i - 1]:
            continue
        changed += 1
        banned = {lamps[i - 1]}
        if i + 1 < n:
            banned.add(lamps[i + 1])
        for colour in "RGB":
            if colour not in banned:
                lamps[i] = colour
                break
    return changed


# --- clause: main :: () -> None ---
def main():
    n, lamps = read_input()
    changed = recolour(n, lamps)
    sys.stdout.write("%d\n%s\n" % (changed, "".join(lamps)))


if __name__ == "__main__":
    main()
