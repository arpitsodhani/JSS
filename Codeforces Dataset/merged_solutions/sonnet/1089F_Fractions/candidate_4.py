# CLAUSE: setup_environment
import sys

def collect_two(n):
    res = []
    div = 2
    cur = n
    while div * div <= cur and len(res) < 2:
        if cur % div == 0:
            res.append(div)
            while cur % div == 0:
                cur //= div
        div += 1 if div == 2 else 2
    if cur > 1 and len(res) < 2:
        res.append(cur)
    return res

def add_parts(target, denominator, rows):
    cap = denominator - 1
    full, rem = divmod(target, cap)
    for _ in range(full):
        rows.append((cap, denominator))
    if rem:
        rows.append((rem, denominator))

# CLAUSE: solve_logic
def answer_for(n):
    primes = collect_two(n)
    if len(primes) != 2:
        return ""

    p = primes[0]
    q = primes[1]

    x = ((n - 1) * pow(p, -1, q)) % q
    y = (n - 1 - x * p) // q

    rows = []
    add_parts(x, n // p, rows)
    add_parts(y, n // q, rows)

    text = ["YES", str(len(rows))]
    for item in rows:
        text.append("{} {}".format(item[0], item[1]))
    return "\n".join(text)

# CLAUSE: finish_program
def main():
    data = sys.stdin.buffer.read().split()
    if data:
        result = answer_for(int(data[0]))
        if result:
            sys.stdout.write(result + "\n")
        else:
            sys.stdout.write("NO\n")

if __name__ == "__main__":
    main()
