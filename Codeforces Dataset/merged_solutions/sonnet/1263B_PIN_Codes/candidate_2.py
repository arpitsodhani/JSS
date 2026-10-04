# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    tokens = sys.stdin.read().split()
    pointer = 0
    tests = int(tokens[pointer])
    pointer += 1
    answer = []

    for _ in range(tests):
        n = int(tokens[pointer])
        pointer += 1
        pins = tokens[pointer:pointer + n]
        pointer += n

        used = set()
        repeated = []
        for i, code in enumerate(pins):
            if code in used:
                repeated.append(i)
            else:
                used.add(code)

        changed = 0
        for i in repeated:
            digits = list(pins[i])
            done = False
            for pos in range(4):
                original = digits[pos]
                for new_digit in "0123456789":
                    if new_digit != original:
                        digits[pos] = new_digit
                        candidate = "".join(digits)
                        if candidate not in used:
                            pins[i] = candidate
                            used.add(candidate)
                            changed += 1
                            done = True
                            break
                if done:
                    break
                digits[pos] = original

        answer.append(str(changed))
        answer.extend(pins)

    sys.stdout.write("\n".join(answer))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
