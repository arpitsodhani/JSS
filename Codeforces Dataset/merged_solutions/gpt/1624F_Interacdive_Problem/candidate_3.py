# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    import sys
    from collections import defaultdict

    def best_query(cand, n):
        best_c = 1
        best_worst = len(cand)
        for c in range(1, n):
            cnt = {}
            worst = 0
            for v in cand:
                q = (v + c) // n
                cnt[q] = cnt.get(q, 0) + 1
                if cnt[q] > worst:
                    worst = cnt[q]
            if worst < best_worst:
                best_worst = worst
                best_c = c
        return best_c

    def main():
        first = sys.stdin.readline().split()
        if not first:
            return

        if len(first) >= 2:
            print(f"! {int(first[0])}")
            return

        n = int(first[0])
        cand = list(range(1, n))

        while len(cand) > 1:
            c = best_query(cand, n)
            print(f"+ {c}", flush=True)
            line = sys.stdin.readline()
            if not line:
                return
            q = int(line)
            cand = [v + c for v in cand if (v + c) // n == q]

        print(f"! {cand[0]}", flush=True)

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
