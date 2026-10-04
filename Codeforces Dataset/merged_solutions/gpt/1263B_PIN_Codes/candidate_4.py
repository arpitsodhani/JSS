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
        idx = 1
        out = []

        for _ in range(t):
            n = int(data[idx])
            idx += 1
            pins = data[idx:idx + n]
            idx += n

            used = set()
            changes = 0

            for i in range(n):
                if pins[i] not in used:
                    used.add(pins[i])
                    continue

                changes += 1
                s = list(pins[i])
                found = False

                for pos in range(4):
                    old = s[pos]
                    for d in "0123456789":
                        if d == old:
                            continue
                        s[pos] = d
                        candidate = "".join(s)
                        if candidate not in used:
                            pins[i] = candidate
                            used.add(candidate)
                            found = True
                            break
                    if found:
                        break
                    s[pos] = old

            out.append(str(changes))
            out.extend(pins)

        sys.stdout.write("\n".join(out))

    if __name__ == "__main__":
        main()

# CLAUSE: finish_program
def main():
    _inner_main()

main()
