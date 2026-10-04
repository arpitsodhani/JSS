import sys


# --- clause: read_input :: () -> list[tuple[list[int], list[tuple[int, int]]]] ---
def read_input():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        a = data[pos:pos + n]
        pos += n
        q = data[pos]
        pos += 1
        queries = []
        for _ in range(q):
            queries.append((data[pos], data[pos + 1]))
            pos += 2
        cases.append((a, queries))
    return cases


# --- clause: exact_root :: (value: int) -> int ---
def exact_root(value):
    if value < 0:
        return -1
    guess = int(value ** 0.5)
    while guess > 0 and guess * guess > value:
        guess -= 1
    while (guess + 1) * (guess + 1) <= value:
        guess += 1
    return guess if guess * guess == value else -1


# --- clause: answer_queries :: (a: list[int], queries: list[tuple[int, int]]) -> list[int] ---
def answer_queries(a, queries):
    counts = {}
    for value in a:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    answers = []
    for x, y in queries:
        disc = x * x - 4 * y
        root = exact_root(disc)
        if root < 0 or (x - root) % 2 != 0:
            answers.append(0)
            continue
        low = (x - root) >> 1
        high = (x + root) >> 1
        if low == high:
            times = counts.get(low, 0)
            answers.append(times * (times - 1) // 2)
        else:
            answers.append(counts.get(low, 0) * counts.get(high, 0))
    return answers


# --- clause: main :: () -> None ---
def main():
    out = []
    for a, queries in read_input():
        out.append(" ".join(map(str, answer_queries(a, queries))))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
