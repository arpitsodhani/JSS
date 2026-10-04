# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    lines = sys.stdin.read().splitlines()
    heading = lines[0] if lines else ""
    text = lines[1] if len(lines) > 1 else ""

    balance = [0] * 256

    for ch in heading:
        if ch != " ":
            balance[ord(ch)] += 1

    possible = True
    for ch in text:
        if ch == " ":
            continue
        index = ord(ch)
        balance[index] -= 1
        if balance[index] < 0:
            possible = False
            break

    sys.stdout.write("YES\n" if possible else "NO\n")

# CLAUSE: finish_program
main()
