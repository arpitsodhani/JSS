# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    import sys

    def main():
        data = sys.stdin.read().split()
        if not data:
            return

        n = int(data[0])
        names = data[1:]

        used = {}
        out = []

        for name in names[:n]:
            if name not in used:
                used[name] = 1
                out.append("OK")
            else:
                k = used[name]
                while True:
                    new_name = name + str(k)
                    if new_name not in used:
                        used[name] = k + 1
                        used[new_name] = 1
                        out.append(new_name)
                        break
                    k += 1

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
