import sys


# --- clause: read_input :: () -> list[tuple[str, int, str]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    rules = [(data[1 + 3 * i].decode(), int(data[2 + 3 * i]), data[3 + 3 * i].decode())
             for i in range(n)]
    return rules


# --- clause: narrow :: (rules: list[tuple[str, int, str]]) -> str ---
def narrow(rules):
    low = -2000000000
    high = 2000000000
    for sign, x, answer in rules:
        yes = answer == "Y"
        if sign == ">":
            if yes:
                if x + 1 > low:
                    low = x + 1
            elif x < high:
                high = x
        elif sign == "<":
            if yes:
                if x - 1 < high:
                    high = x - 1
            elif x > low:
                low = x
        elif sign == ">=":
            if yes:
                if x > low:
                    low = x
            elif x - 1 < high:
                high = x - 1
        else:
            if yes:
                if x < high:
                    high = x
            elif x + 1 > low:
                low = x + 1
    if low > high:
        return "Impossible"
    return str(low)


# --- clause: main :: () -> None ---
def main():
    rules = read_input()
    sys.stdout.write(narrow(rules) + "\n")


if __name__ == "__main__":
    main()
