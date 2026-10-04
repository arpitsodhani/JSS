import sys


# --- clause: read_input :: () -> tuple[int, int, list[int], list[int], list[int]] ---
def read_input():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    ones = []
    twos = []
    threes = []
    pos = 2
    for _ in range(n):
        weight = int(data[pos])
        cost = int(data[pos + 1])
        pos += 2
        if weight == 1:
            ones.append(cost)
        elif weight == 2:
            twos.append(cost)
        else:
            threes.append(cost)
    ones.sort(reverse=True)
    twos.sort(reverse=True)
    threes.sort(reverse=True)
    return n, m, ones, twos, threes


# --- clause: light_table :: (m: int, ones: list[int], twos: list[int]) -> list[int] ---
def light_table(m, ones, twos):
    pre_one = [0] * (len(ones) + 1)
    for i, cost in enumerate(ones):
        pre_one[i + 1] = pre_one[i] + cost
    pre_two = [0] * (len(twos) + 1)
    for i in range(len(twos)):
        pre_two[i + 1] = pre_two[i] + twos[i]
    top_one = len(ones)
    top_two = len(twos)
    best = [0] * (m + 1)
    pairs = 0
    for cap in range(m + 1):
        singles = cap - 2 * pairs
        if singles > top_one:
            singles = top_one
        here = pre_two[pairs] + pre_one[singles]
        while pairs < top_two and 2 * (pairs + 1) <= cap:
            spare = cap - 2 * (pairs + 1)
            if spare > top_one:
                spare = top_one
            other = pre_two[pairs + 1] + pre_one[spare]
            if here > other:
                break
            pairs += 1
            here = other
        best[cap] = here
    return best


# --- clause: best_value :: (m: int, threes: list[int], best: list[int]) -> int ---
def best_value(m, threes, best):
    total = 0
    answer = best[m]
    for count in range(1, len(threes) + 1):
        used = 3 * count
        if used > m:
            break
        total += threes[count - 1]
        here = total + best[m - used]
        if here > answer:
            answer = here
    return answer


# --- clause: main :: () -> None ---
def main():
    n, m, ones, twos, threes = read_input()
    best = light_table(m, ones, twos)
    sys.stdout.write(str(best_value(m, threes, best)) + "\n")


if __name__ == "__main__":
    main()
