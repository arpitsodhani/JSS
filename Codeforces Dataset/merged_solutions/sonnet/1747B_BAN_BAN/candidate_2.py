import sys


# --- clause: read_input :: () -> list[int] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    return list(map(int, data[1:1 + t]))


# --- clause: plan_swaps :: (n: int) -> list[str] ---
def plan_swaps(n):
    moves = -(-n // 2)
    out = [str(moves)]
    i = 0
    while i < moves:
        out.append(str(3 * i + 2) + " " + str(3 * (n - i)))
        i += 1
    return out


# --- clause: main :: () -> None ---
def main():
    out = []
    for n in read_input():
        out.extend(plan_swaps(n))
    sys.stdout.write("%s\n" % "\n".join(out))


if __name__ == "__main__":
    main()
