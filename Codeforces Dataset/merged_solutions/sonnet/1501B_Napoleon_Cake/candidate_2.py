import sys


# --- clause: read_input :: () -> list[list[int]] ---
def read_input():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    t = tokens[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = tokens[pos]
        pos += 1
        cases.append(tokens[pos:pos + n])
        pos += n
    return cases


# --- clause: soaked_layers :: (cream: list[int]) -> list[int] ---
def soaked_layers(cream):
    n = len(cream)
    wet = [0] * n
    reach = 0
    for i in range(n - 1, -1, -1):
        if cream[i] > reach:
            reach = cream[i]
        if reach > 0:
            wet[i] = 1
            reach -= 1
    return wet


# --- clause: main :: () -> None ---
def main():
    lines = []
    for cream in read_input():
        lines.append(" ".join(map(str, soaked_layers(cream))))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
