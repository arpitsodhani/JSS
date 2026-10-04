import sys


# --- clause: read_input :: () -> list[tuple[str, int, str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    rules = list()
    for i in range(n):
        rules.append((data[1 + 3 * i].decode(), int(data[2 + 3 * i]), data[3 + 3 * i].decode()))
    return rules


# --- clause: narrow :: (rules: list[tuple[str, int, str]]) -> str ---
def narrow(rules):
    lows = [-2000000000]
    highs = [2000000000]
    for sign, x, answer in rules:
        yes = answer == "Y"
        if sign == ">":
            key = ("low", x + 1) if yes else ("high", x)
        elif sign == "<":
            key = ("high", x - 1) if yes else ("low", x)
        elif sign == ">=":
            key = ("low", x) if yes else ("high", x - 1)
        else:
            key = ("high", x) if yes else ("low", x + 1)
        if key[0] == "low":
            lows.append(key[1])
        else:
            highs.append(key[1])
    low = max(lows)
    high = min(highs)
    del lows, highs
    if low > high:
        return "Impossible"
    return str(low)


# --- clause: main :: () -> None ---
def main():
    sys.stdout.write(narrow(read_input()) + "\n")


if __name__ == "__main__":
    main()
