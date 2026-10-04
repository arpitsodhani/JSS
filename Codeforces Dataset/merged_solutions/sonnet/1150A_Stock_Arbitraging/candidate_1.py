import sys


# --- clause: read_input :: () -> tuple[int, int, int, list[int], list[int]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    m = data[1]
    r = data[2]
    buy = data[3:3 + n]
    sell = data[3 + n:3 + n + m]
    return n, m, r, buy, sell


# --- clause: best_money :: (r: int, buy: list[int], sell: list[int]) -> int ---
def best_money(r, buy, sell):
    cheapest = min(buy)
    dearest = max(sell)
    if dearest <= cheapest:
        return r
    shares = r // cheapest
    return r - shares * cheapest + shares * dearest


# --- clause: main :: () -> None ---
def main():
    n, m, r, buy, sell = read_input()
    sys.stdout.write(str(best_money(r, buy, sell)) + "\n")


if __name__ == "__main__":
    main()
