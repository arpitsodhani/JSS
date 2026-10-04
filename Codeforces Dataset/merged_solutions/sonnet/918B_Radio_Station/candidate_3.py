import sys


# --- clause: read_input :: () -> tuple[int, int, list[bytes]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    return n, m, data[2:2 + 2 * n + 2 * m]


# --- clause: annotate :: (n: int, m: int, rest: list[bytes]) -> list[str] ---
def annotate(n, m, rest):
    out = []
    base = 2 * n
    for i in range(m):
        command = rest[base + 2 * i].decode()
        target = rest[base + 2 * i + 1]
        wanted = target[:-1]
        label = ""
        for j in range(n):
            if rest[2 * j + 1] == wanted:
                label = rest[2 * j].decode()
                break
        out.append(command + " " + target.decode() + " #" + label)
    return out


# --- clause: main :: () -> None ---
def main():
    n, m, rest = read_input()
    print("\n".join(annotate(n, m, rest)))


if __name__ == "__main__":
    main()
