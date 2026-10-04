"""907A accepts any car sizes satisfying every bear's and Masha's condition."""


def check_for(stdin, expected):
    v1, v2, v3, vm = (int(v) for v in stdin.split())
    possible = expected.strip() != "-1"

    def check(out):
        rows = [line.strip() for line in out.split("\n") if line.strip()]
        if not possible:
            assert rows[0] == "-1", "printed cars where none exist"
            return
        assert rows[0] != "-1", "cars exist but -1 was printed"
        big, middle, small = (int(v) for v in rows[:3])
        assert big > middle > small, "the cars are not strictly decreasing"
        assert big >= v1 and middle >= v2 and small >= v3, "a bear does not fit"
        assert big <= 2 * v1 and middle <= 2 * v2 and small <= 2 * v3, "a bear does not like the car"
        for size in (big, middle, small):
            assert size >= vm, "Masha cannot climb in"
        assert small <= 2 * vm, "Masha does not like the smallest car"
        assert big > 2 * vm and middle > 2 * vm, "Masha likes a car she should not"

    return check
