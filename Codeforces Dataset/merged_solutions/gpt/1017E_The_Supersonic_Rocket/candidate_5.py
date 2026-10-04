# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        def cross(a, b, c):
            return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

        def convex_hull(points):
            points = sorted(points)
            if len(points) <= 1:
                return points

            lower = []
            for p in points:
                while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                    lower.pop()
                lower.append(p)

            upper = []
            for p in reversed(points):
                while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
                    upper.pop()
                upper.append(p)

            return lower[:-1] + upper[:-1]

        def dist2(a, b):
            dx = a[0] - b[0]
            dy = a[1] - b[1]
            return dx * dx + dy * dy

        def signature(poly):
            n = len(poly)
            res = []
            for i in range(n):
                a = poly[i]
                b = poly[(i + 1) % n]
                c = poly[(i + 2) % n]
                e1 = (b[0] - a[0], b[1] - a[1])
                e2 = (c[0] - b[0], c[1] - b[1])
                res.append((
                    e1[0] * e1[0] + e1[1] * e1[1],
                    e1[0] * e2[0] + e1[1] * e2[1],
                    e1[0] * e2[1] - e1[1] * e2[0]
                ))
            return res

        def contains_cyclic(a, b):
            pattern = a
            text = b + b
            pi = [0] * len(pattern)

            for i in range(1, len(pattern)):
                j = pi[i - 1]
                while j and pattern[i] != pattern[j]:
                    j = pi[j - 1]
                if pattern[i] == pattern[j]:
                    j += 1
                pi[i] = j

            j = 0
            for x in text:
                while j and x != pattern[j]:
                    j = pi[j - 1]
                if x == pattern[j]:
                    j += 1
                if j == len(pattern):
                    return True
            return False

        def same_shape(a, b):
            a = convex_hull(a)
            b = convex_hull(b)

            if len(a) != len(b):
                return False

            n = len(a)
            if n == 1:
                return True
            if n == 2:
                return dist2(a[0], a[1]) == dist2(b[0], b[1])

            return contains_cyclic(signature(a), signature(b))

        def main():
            data = list(map(int, sys.stdin.buffer.read().split()))
            if not data:
                return

            n, m = data[0], data[1]
            idx = 2

            a = []
            for _ in range(n):
                a.append((data[idx], data[idx + 1]))
                idx += 2

            b = []
            for _ in range(m):
                b.append((data[idx], data[idx + 1]))
                idx += 2

            print("YES" if same_shape(a, b) else "NO")

        if __name__ == "__main__":
            main()

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
