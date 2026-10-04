# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        k = int(input())

        if k % 2 == 0:
            print("NO")
        elif k == 1:
            print("YES")
            print(2, 1)
            print(1, 2)
        else:
            n = 2 * (k + 2)
            edges = []

            def build(offset):
                root = offset + 1
                others = list(range(offset + 2, offset + k + 3))

                for v in others[:k - 1]:
                    edges.append((root, v))

                removed = set()
                for i in range(0, k - 1, 2):
                    a = others[i]
                    b = others[i + 1]
                    removed.add((min(a, b), max(a, b)))

                for i in range(len(others)):
                    for j in range(i + 1, len(others)):
                        a, b = others[i], others[j]
                        if (min(a, b), max(a, b)) not in removed:
                            edges.append((a, b))

            build(0)
            build(k + 2)
            edges.append((1, k + 3))

            print("YES")
            print(n, len(edges))
            for a, b in edges:
                print(a, b)

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
