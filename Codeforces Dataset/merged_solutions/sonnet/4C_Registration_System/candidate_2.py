import sys


# --- clause: read_input :: () -> list[str] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    return [data[1 + i].decode() for i in range(n)]


# --- clause: register_all :: (names: list[str]) -> list[str] ---
def register_all(names):
    used = {}
    replies = []
    for name in names:
        count = used.get(name, 0)
        if count:
            replies.append("%s%d" % (name, count))
        else:
            replies.append("OK")
        used[name] = count + 1
    return replies


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write("\n".join(register_all(read_input())) + "\n")


if __name__ == "__main__":
    main()
