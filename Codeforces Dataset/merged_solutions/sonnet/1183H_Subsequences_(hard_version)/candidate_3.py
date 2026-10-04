# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def add_character(ways, seen, char_index, upto):
    length = upto
    while length:
        source = ways[length - 1]
        ways[length] = ways[length] + source - seen[char_index][length]
        seen[char_index][length] = source
        length -= 1

def minimum_cost(n, k, s):
    ways = [1] + [0] * n
    seen = [[0 for _ in range(n + 1)] for _ in range(26)]

    position = 1
    for letter in s:
        add_character(ways, seen, ord(letter) - 97, position)
        position += 1

    cost = 0
    missing = k
    length = n
    while length >= 0:
        amount = ways[length]
        if amount >= missing:
            return cost + missing * (n - length)
        cost += amount * (n - length)
        missing -= amount
        length -= 1
    return -1

def main():
    tokens = sys.stdin.buffer.read().split()
    n = int(tokens[0])
    k = int(tokens[1])
    s = tokens[2].decode()
    print(minimum_cost(n, k, s))

# CLAUSE: finish_program
main()
