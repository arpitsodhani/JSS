# CLAUSE: setup_environment
import sys

MOD = 998244353

# CLAUSE: solve_logic
def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    n = data[0]
    raw = []
    max_health = 0
    p = 1

    for _ in range(n):
        op = data[p]
        p += 1
        if op == 3:
            raw.append((op, 0))
        else:
            x = data[p]
            p += 1
            raw.append((op, x))
            if op == 1 and x > max_health:
                max_health = x

    size = max_health + 2
    counts = [0] * size
    total_damage = 0
    cap = max_health + 1

    for op, x in raw:
        if op == 1:
            counts[x] = (counts[x] + 1) % MOD
        elif op == 2:
            if x >= max_health:
                counts = [0] * size
            else:
                moved = [0] * size
                for hp in range(x + 1, size):
                    if counts[hp]:
                        moved[hp - x] = counts[hp]
                counts = moved
            total_damage = min(cap, total_damage + x)
        else:
            copied = counts[:]
            if total_damage < size:
                for hp in range(total_damage + 1, size):
                    if counts[hp]:
                        copied[hp - total_damage] = (copied[hp - total_damage] + counts[hp]) % MOD
            counts = copied
            total_damage = min(cap, total_damage * 2)

    sys.stdout.write(str(sum(counts) % MOD))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
