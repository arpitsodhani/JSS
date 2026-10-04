# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def emit(lines, ops):
    lines.append(str(len(ops)))
    for pair in ops:
        lines.append("{} {}".format(pair[0], pair[1]))

def main():
    raw = sys.stdin.buffer.read().split()
    q = int(raw[0])
    k = 1
    lines = []

    for _ in range(q):
        n = int(raw[k])
        m = int(raw[k + 1])
        k += 2

        health = []
        ids = []
        for idx in range(n):
            health.append(int(raw[k]))
            ids.append(idx + 1)
            k += 1

        order = sorted(range(n), key=health.__getitem__)
        sorted_health = [health[i] for i in order]
        sorted_ids = [ids[i] for i in order]

        if n == 1:
            lines.append("0" if m == 1 else "-1")
            continue

        if m > 0:
            if m > n // 2:
                lines.append("-1")
                continue
            moves = []
            for i in range(n - m):
                moves.append((sorted_ids[i + m], sorted_ids[i]))
            emit(lines, moves)
            continue

        if sum(sorted_health[:-1]) < sorted_health[-1]:
            lines.append("-1")
            continue

        suffix = 0
        pivot = n - 2
        while True:
            suffix += sorted_health[pivot]
            if suffix >= sorted_health[-1]:
                break
            pivot -= 1

        leader = sorted_ids[-1]
        moves = []
        moves.extend((sorted_ids[i + 1], sorted_ids[i]) for i in range(pivot))
        moves.append((leader, sorted_ids[pivot]))
        moves.extend((sorted_ids[i], leader) for i in range(pivot + 1, n - 1))
        emit(lines, moves)

# CLAUSE: finish_program
    sys.stdout.write("\n".join(lines))

if __name__ == "__main__":
    main()
