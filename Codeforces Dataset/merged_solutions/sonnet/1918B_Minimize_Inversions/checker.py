"""1918B accepts any rearrangement of the (a_i, b_i) pairs with the fewest total
inversions.

Sorting the pairs by a is optimal, so the checker uses that as the reference and
then confirms the printed arrays are a permutation of the same pairs with the
same inversion total.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    t = data[0]
    pos = 1
    cases = []
    for _ in range(t):
        n = data[pos]
        pos += 1
        a = data[pos:pos + n]
        pos += n
        b = data[pos:pos + n]
        pos += n
        cases.append((a, b))

    def inversions(seq):
        n = len(seq)
        return sum(1 for i in range(n) for j in range(i + 1, n) if seq[i] > seq[j])

    def check(out):
        tokens = [int(v) for v in out.split()]
        at = 0
        for a, b in cases:
            n = len(a)
            first = tokens[at:at + n]
            at += n
            second = tokens[at:at + n]
            at += n
            assert sorted(zip(first, second)) == sorted(zip(a, b)), "pairs were not preserved"
            best_pairs = sorted(zip(a, b))
            best = inversions([p[0] for p in best_pairs]) + inversions([p[1] for p in best_pairs])
            here = inversions(first) + inversions(second)
            assert here == best, f"{here} inversions, the minimum is {best}"
        assert at == len(tokens), "extra output"

    return check
