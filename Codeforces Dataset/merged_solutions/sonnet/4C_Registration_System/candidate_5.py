import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    return [data[1 + i].decode() for i in range(n)]


# --- clause: register_all :: (names: list[str]) -> list[str] ---
def register_all(names):
    seen = dict()
    out = list()
    for name in names:
        if name in seen:
            count = seen[name]
            seen[name] = count + 1
            out.append(name + str(count))
        else:
            seen[name] = 1
            out.append("OK")
    return out


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("\n".join(register_all(read_input())) + "\n")


if __name__ == "__main__":
    main()
