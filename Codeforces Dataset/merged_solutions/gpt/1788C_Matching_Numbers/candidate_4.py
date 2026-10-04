# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def main():
        data = sys.stdin.read().strip().split()
        if not data:
            return
        t = int(data[0])
        out = []
        for idx in range(1, t + 1):
            n = int(data[idx])
            if n % 2 == 0:
                out.append("No")
                continue
            out.append("Yes")
            k = (n + 1) // 2
            for i in range(1, k + 1):
                out.append(f"{i} {3 * k - i}")
            for i in range(k + 1, n + 1):
                out.append(f"{i} {5 * k - i - 1}")
        print("\n".join(out))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
