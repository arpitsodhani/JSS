"""1762B accepts any sequence of at most n operations that leaves the array good.

An array is good when every pair's maximum divides by its minimum; the checker
replays the printed operations and tests that on the sorted result.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        cases.append(data[pos:pos + n])
        pos += n

    def check(out):
        tokens = [int(v) for v in out.split()]
        at = 0
        for a in cases:
            n = len(a)
            values = list(a)
            count = tokens[at]
            at += 1
            assert 0 <= count <= n, f"{count} operations for n={n}"
            for _ in range(count):
                index = tokens[at]
                add = tokens[at + 1]
                at += 2
                assert 1 <= index <= n, f"index {index} out of range"
                assert 0 <= add <= values[index - 1], (
                    f"x={add} is not in [0, {values[index - 1]}]")
                values[index - 1] += add
                assert values[index - 1] <= 10 ** 18, "value above 1e18"
            order = sorted(values)
            for i in range(n - 1):
                assert order[i + 1] % order[i] == 0, (
                    f"{order[i + 1]} is not a multiple of {order[i]}")

    return check
