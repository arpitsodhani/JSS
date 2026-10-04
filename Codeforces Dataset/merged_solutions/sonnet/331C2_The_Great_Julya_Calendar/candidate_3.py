# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def largest_digit_and_last_nine(value):
    chars = str(value)
    best = 0
    last_nine = -1
    for i, ch in enumerate(chars):
        d = ord(ch) - 48
        if d > best:
            best = d
        if ch == "9":
            last_nine = i
    return chars, best, last_nine

def main():
    n = int(sys.stdin.buffer.readline())
    total = 0
    while n > 0:
        chars, best, last_nine = largest_digit_and_last_nine(n)
        count = 1
        if best == 9:
            p = len(chars) - last_nine - 1
            block = 10 ** p
            count = (n % block) // 9 + 1
        n -= best * count
        total += count

# CLAUSE: finish_program
    print(total)

if __name__ == "__main__":
    main()
