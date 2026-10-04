import sys


# --- clause: read_input :: () -> tuple[int, list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    buttons = []
    for token in data[1:n + 1]:
        buttons.append(int(token))
    return n, buttons


# --- clause: fastened_well :: (n: int, buttons: list[int]) -> str ---
def fastened_well(n, buttons):
    done = 0
    index = 0
    while index < n:
        done += buttons[index]
        index += 1
    if n == 1:
        if done == 1:
            return "YES"
        return "NO"
    if done == n - 1:
        return "YES"
    return "NO"


# --- clause: main :: () -> None ---
def main():
    n, buttons = read_input()
    print(fastened_well(n, buttons))


if __name__ == "__main__":
    main()
