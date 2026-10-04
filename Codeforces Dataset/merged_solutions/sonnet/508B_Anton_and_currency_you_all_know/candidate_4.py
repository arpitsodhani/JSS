# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def main():
    text = sys.stdin.readline().strip()
    last = text[-1]
    even_positions = [i for i, ch in enumerate(text[:-1]) if int(ch) % 2 == 0]

    if not even_positions:
        sys.stdout.write("-1\n")
        return

    chosen = even_positions[-1]
    for i in even_positions:
        if text[i] < last:
            chosen = i
            break

    pieces = list(text)
    pieces[chosen], pieces[-1] = pieces[-1], pieces[chosen]
    sys.stdout.write("".join(pieces) + "\n")

# CLAUSE: finish_program
main()
