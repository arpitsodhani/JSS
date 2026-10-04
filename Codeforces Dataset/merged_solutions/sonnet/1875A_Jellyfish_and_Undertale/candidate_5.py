import sys


# --- clause: read_input :: () -> list[tuple[int, int, list[int]]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    pos = 0
    t = int(data[pos])
    pos += 1
    cases = []
    for _ in range(t):
        a = int(data[pos])
        pos += 1
        b = int(data[pos])
        pos += 1
        n = int(data[pos])
        pos += 1
        tools = [int(token) for token in data[pos:pos + n]]
        pos += n
        cases.append((a, b, tools))
    return cases


# --- clause: survival_time :: (a: int, b: int, tools: list[int]) -> int ---
def survival_time(a, b, tools):
    total = b
    cap = a - 1
    for gain in tools:
        total += cap if cap < gain else gain
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, b, tools in read_input():
        out.append(str(survival_time(a, b, tools)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
