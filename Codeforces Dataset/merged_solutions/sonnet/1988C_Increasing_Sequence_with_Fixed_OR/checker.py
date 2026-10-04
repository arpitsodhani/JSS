"""1988C accepts any longest sequence, so the printed one is checked itself.

It has to be strictly increasing, bounded by n, have every adjacent OR equal to
n, and match the reference length.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    values = data[1:1 + data[0]]
    wanted = [int(line) for line in expected.split("\n")[::2] if line.strip()]

    def check(out):
        rows = [line for line in out.split("\n") if line.strip()]
        at = 0
        for case, n in enumerate(values):
            k = int(rows[at])
            seq = [int(v) for v in rows[at + 1].split()]
            at += 2
            assert len(seq) == k, f"n={n}: said {k} values, printed {len(seq)}"
            assert k == wanted[case], f"n={n}: length {k}, longest is {wanted[case]}"
            assert all(1 <= v <= n for v in seq), f"n={n}: a value is outside 1..n"
            assert all(seq[i] < seq[i + 1] for i in range(k - 1)), f"n={n}: not increasing"
            for i in range(1, k):
                assert seq[i] | seq[i - 1] == n, f"n={n}: {seq[i - 1]} | {seq[i]} != n"

    return check
