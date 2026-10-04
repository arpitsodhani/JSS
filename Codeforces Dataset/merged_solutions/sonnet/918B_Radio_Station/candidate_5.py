import sys


# --- clause: read_input :: () -> tuple[int, int, list[bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    return n, m, data[2:]


# --- clause: annotate :: (n: int, m: int, rest: list[bytes]) -> list[str] ---
def annotate(n, m, rest):
    out = []
    base = 2 * n
    for i in range(m):
        command = rest[base + 2 * i].decode()
        target = rest[base + 2 * i + 1]
        wanted = target[:-1]
        label = ""
        j = 0
        while j < n:
            if rest[2 * j + 1] == wanted:
                label = rest[2 * j].decode()
                break
            j += 1
        out.append(command + " " + target.decode() + " #" + label)
    return out


# --- clause: main :: () -> None ---
def main():
    n, m, rest = read_input()
    sys.stdout.write("\n".join(annotate(n, m, rest)) + "\n")


if __name__ == "__main__":
    main()
