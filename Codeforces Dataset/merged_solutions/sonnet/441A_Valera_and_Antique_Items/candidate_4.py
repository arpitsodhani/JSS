import sys


# --- clause: read_input :: () -> tuple[int, int, list[list[int]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    v = data[1]
    pos = 2
    sellers = []
    for _ in range(n):
        k = data[pos]
        pos += 1
        sellers.append(data[pos:pos + k])
        pos += k
    return n, v, sellers

# --- clause: reachable_sellers :: (v: int, sellers: list[list[int]]) -> list[int] ---
def reachable_sellers(v, sellers):
    good = []
    number = 0
    for prices in sellers:
        number += 1
        cheapest = prices[0]
        for price in prices:
            if price < cheapest:
                cheapest = price
        if cheapest < v:
            good.append(number)
    return good

# --- clause: main :: () -> None ---
def main():
    n, v, sellers = read_input()
    good = reachable_sellers(v, sellers)
    sys.stdout.write(str(len(good)) + "\n" + " ".join(map(str, good)) + "\n")


if __name__ == "__main__":
    main()
