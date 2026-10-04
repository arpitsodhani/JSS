# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.buffer.read().split()))
        if not data:
            sys.exit()

        it = iter(data)
        n = next(it)
        k = next(it)
        s = next(it)
        t = next(it)

        cars = []
        for _ in range(n):
            c = next(it)
            v = next(it)
            cars.append((c, v))

        stations = [next(it) for _ in range(k)]
        stations.sort()

        points = [0] + stations + [s]
        segments = [points[i] - points[i - 1] for i in range(1, len(points))]
        max_segment = max(segments)

        def ok(cap):
            if cap < max_segment:
                return False
            total = 0
            for d in segments:
                if cap >= 2 * d:
                    total += d
                else:
                    total += 3 * d - cap
                if total > t:
                    return False
            return total <= t

        lo, hi = max_segment, 10 ** 9
        while lo < hi:
            mid = (lo + hi) // 2
            if ok(mid):
                hi = mid
            else:
                lo = mid + 1

        need = lo
        ans = min((c for c, v in cars if v >= need), default=-1)
        print(ans)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
