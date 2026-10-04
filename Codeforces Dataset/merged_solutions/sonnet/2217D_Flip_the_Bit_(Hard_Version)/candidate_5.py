# CLAUSE: setup_environment
import sys

def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    cases = values[0]
    p = 1
    output = []

# CLAUSE: solve_logic
    for _ in range(cases):
        n, k = values[p], values[p + 1]
        p += 2

        arr = values[p:p + n]
        p += n

        special = sorted(values[p:p + k])
        p += k

        wanted = arr[special[0] - 1]
        limits = [0] + special + [n + 1]
        changes_by_zone = []
        run_count = 0
        prev = 0

        for left, right in zip(limits, limits[1:]):
            zone_changes = 0
            start = left + 1
            stop = right + 1

            for i in range(start, stop):
                cur = 0
                if i <= n:
                    cur = arr[i - 1] ^ wanted

                if cur != prev:
                    zone_changes += 1
                    if cur == 1:
                        run_count += 1

                prev = cur

            changes_by_zone.append(zone_changes)

        local_need = max(changes_by_zone)
        output.append(str(run_count if run_count > local_need else local_need))

# CLAUSE: finish_program
    sys.stdout.write("\n".join(output))

if __name__ == "__main__":
    main()
