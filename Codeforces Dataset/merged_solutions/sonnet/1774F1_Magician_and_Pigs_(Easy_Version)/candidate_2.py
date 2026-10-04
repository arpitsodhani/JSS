# CLAUSE: setup_environment
import sys
from collections import defaultdict

MOD = 998244353

# CLAUSE: solve_logic
def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    n = int(data[0])
    pos = 1
    operations = []
    largest = 0

    for _ in range(n):
        t = int(data[pos])
        pos += 1
        if t == 3:
            operations.append((3, 0))
        else:
            x = int(data[pos])
            pos += 1
            operations.append((t, x))
            if t == 1 and x > largest:
                largest = x

    limit = largest + 1
    damage = 0
    alive = defaultdict(int)

    for t, x in operations:
        if t == 1:
            alive[x] = (alive[x] + 1) % MOD
        elif t == 2:
            if x >= largest:
                alive.clear()
            else:
                nxt = defaultdict(int)
                for hp, ways in alive.items():
                    if hp > x:
                        nxt[hp - x] = (nxt[hp - x] + ways) % MOD
                alive = nxt
            damage = min(limit, damage + x)
        else:
            nxt = defaultdict(int)
            for hp, ways in alive.items():
                nxt[hp] = (nxt[hp] + ways) % MOD
                if hp > damage:
                    nxt[hp - damage] = (nxt[hp - damage] + ways) % MOD
            alive = nxt
            damage = min(limit, damage * 2)

    sys.stdout.write(str(sum(alive.values()) % MOD))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
