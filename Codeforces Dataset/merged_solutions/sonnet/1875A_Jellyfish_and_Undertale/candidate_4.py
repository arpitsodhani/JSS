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
        b = int(data[pos + 1])
        n = int(data[pos + 2])
        pos += 3
        tools = [int(data[pos + i]) for i in range(n)]
        pos += n
        cases.append((a, b, tools))
    return cases


# --- clause: survival_time :: (a: int, b: int, tools: list[int]) -> int ---
def survival_time(a, b, tools):
    cap = a - 1
    total = b
    index = 0
    while index < len(tools):
        gain = tools[index]
        if gain > cap:
            gain = cap
        total += gain
        index += 1
    return total


# --- clause: main :: () -> None ---
def main():
    out = []
    for case in read_input():
        out.append(str(survival_time(case[0], case[1], case[2])))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
