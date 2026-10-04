# CLAUSE: setup_environment
import sys

def sum_digits_text(n):
    return sum(ord(c) - 48 for c in str(n))

# CLAUSE: solve_logic
def main():
    raw = sys.stdin.buffer.read().split()
    q = int(raw[0])
    numbers = tuple(int(part) for part in raw[1:q + 1])
    need = max(numbers) if numbers else 0
    prefix = [0]
    append = prefix.append
    current = 0
    for value in range(1, need + 1):
        current += sum_digits_text(value)
        append(current)
    result = [str(prefix[value]) for value in numbers]
    print("\n".join(result))

# CLAUSE: finish_program
if __name__ == "__main__":
    main()
