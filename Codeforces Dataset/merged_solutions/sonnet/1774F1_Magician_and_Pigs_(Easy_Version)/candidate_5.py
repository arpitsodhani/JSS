# CLAUSE: setup_environment
import sys

MOD = 998244353

# CLAUSE: solve_logic
def normalize(items):
    merged = {}
    for hp, ways in items:
        if ways:
            merged[hp] = (merged.get(hp, 0) + ways) % MOD
    return [(hp, ways) for hp, ways in merged.items() if ways]

def main():
    stream = sys.stdin.buffer
    first = stream.readline()
    if not first:
        return

    n = int(first)
    operations = []
    highest = 0

    for _ in range(n):
        row = stream.readline().split()
        typ = int(row[0])
        if typ == 3:
            operations.append((3, 0))
        else:
            val = int(row[1])
            operations.append((typ, val))
            if typ == 1 and val > highest:
                highest = val

    pigs = []
    accumulated = 0
    cap = highest + 1

    for typ, val in operations:
        if typ == 1:
            pigs.append((val, 1))
            pigs = normalize(pigs)
        elif typ == 2:
            if val >= highest:
                pigs = []
            else:
                pigs = normalize((hp - val, ways) for hp, ways in pigs if hp > val)
            accumulated = min(cap, accumulated + val)
        else:
            added = []
            for hp, ways in pigs:
                added.append((hp, ways))
                if hp > accumulated:
                    added.append((hp - accumulated, ways))
            pigs = normalize(added)
            accumulated = min(cap, accumulated * 2)

    answer = 0
    for _, ways in pigs:
        answer = (answer + ways) % MOD
    print(answer)

# CLAUSE: finish_program
main()
