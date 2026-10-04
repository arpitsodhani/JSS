"""1176D accepts any array a that produces the given b.

The printed array is pushed back through the statement's rules — the a_i-th
prime for a prime a_i, the greatest proper divisor otherwise — and the two
multisets are compared.
"""


def check_for(stdin, expected):
    data = [int(v) for v in stdin.split()]
    n = data[0]
    b = sorted(data[1:1 + 2 * n])
    limit = max(b)
    sieve = bytearray([1]) * (limit + 1)
    sieve[0] = 0
    sieve[1] = 0
    step = 2
    while step * step <= limit:
        if sieve[step]:
            sieve[step * step::step] = bytearray(len(range(step * step, limit + 1, step)))
        step += 1
    primes = [value for value in range(2, limit + 1) if sieve[value]]

    def check(out):
        a = [int(v) for v in out.split()]
        assert len(a) == n, f"expected {n} values, got {len(a)}"
        built = []
        for value in a:
            assert 2 <= value <= 200000, f"{value} outside 2..2*10^5"
            built.append(value)
            if sieve[value]:
                assert value <= len(primes), f"the {value}-th prime is beyond the input range"
                built.append(primes[value - 1])
            else:
                divisor = 2
                while value % divisor:
                    divisor += 1
                built.append(value // divisor)
        assert sorted(built) == b, "the array does not produce b"

    return check
