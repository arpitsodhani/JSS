# CLAUSE: setup_environment
import sys

MOD = 998244353

# CLAUSE: solve_logic
def shifted_after_hit(state, hit):
    result = {}
    for hp, amount in state.items():
        if hp > hit:
            nh = hp - hit
            result[nh] = (result.get(nh, 0) + amount) % MOD
    return result

def doubled_sequence(state, total_hit):
    result = {}
    for hp, amount in state.items():
        result[hp] = (result.get(hp, 0) + amount) % MOD
        if hp > total_hit:
            nh = hp - total_hit
            result[nh] = (result.get(nh, 0) + amount) % MOD
    return result

def main():
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    operations = []
    max_hp = 0
    i = 1

    while len(operations) < n:
        kind = int(tokens[i])
        i += 1
        value = 0
        if kind != 3:
            value = int(tokens[i])
            i += 1
            if kind == 1:
                max_hp = max(max_hp, value)
        operations.append((kind, value))

    pigs = {}
    total_hit = 0
    cap = max_hp + 1

    for kind, value in operations:
        if kind == 1:
            pigs[value] = (pigs.get(value, 0) + 1) % MOD
        elif kind == 2:
            pigs = {} if value >= max_hp else shifted_after_hit(pigs, value)
            total_hit = min(cap, total_hit + value)
        else:
            pigs = doubled_sequence(pigs, total_hit)
            total_hit = min(cap, total_hit + total_hit)

    print(sum(pigs.values()) % MOD)

# CLAUSE: finish_program
main()
