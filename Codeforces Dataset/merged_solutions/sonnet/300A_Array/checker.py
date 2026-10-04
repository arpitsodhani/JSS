"""300A accepts any split into a negative-product, positive-product and
zero-product set covering every element exactly once."""


def check_for(stdin, expected):
    tokens = [int(v) for v in stdin.split()]
    n = tokens[0]
    values = tokens[1:1 + n]

    def check(out):
        rows = [line.split() for line in out.strip().split("\n")]
        assert len(rows) == 3, f"expected 3 lines, got {len(rows)}"
        pool = list(values)
        products = []
        for row in rows:
            count = int(row[0])
            assert count > 0, "each set must be non-empty"
            picks = [int(v) for v in row[1:]]
            assert len(picks) == count, "count does not match the listed elements"
            for v in picks:
                assert v in pool, f"{v} is not available"
                pool.remove(v)
            product = 1
            for v in picks:
                product *= v
            products.append(product)
        assert not pool, f"{len(pool)} elements were never placed"
        assert products[0] < 0, "the first product must be negative"
        assert products[1] > 0, "the second product must be positive"
        assert products[2] == 0, "the third product must be zero"

    return check
