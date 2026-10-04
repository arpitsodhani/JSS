import sys

MOD = 998244353

def main():
    input = sys.stdin.readline
    n = int(input())
    ops = []
    total_damage = 0
    pigs = []

    for _ in range(n):
        parts = list(map(int, input().split()))
        if parts[0] == 1:
            x = parts[1]
            ops.append((1, x))
            pigs.append([x + total_damage, 1])
        elif parts[0] == 2:
            x = parts[1]
            ops.append((2, x))
            total_damage += x
        else:
            old_ops = ops[:]
            shift = total_damage
            for op in old_ops:
                if op[0] == 1:
                    pigs.append([op[1] + total_damage, 1])
                else:
                    total_damage += op[1]
            ops += old_ops

            alive = []
            for hp, cnt in pigs:
                if hp > total_damage:
                    alive.append([hp, cnt])
            pigs = alive

    ans = 0
    for hp, cnt in pigs:
        if hp > total_damage:
            ans = (ans + cnt) % MOD

    print(ans)

if __name__ == "__main__":
    main()
