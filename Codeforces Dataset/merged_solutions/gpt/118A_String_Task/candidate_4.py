# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _inner_main():
    s = input().strip()
    vowels = set("aoyeui")
    result = []

    for ch in s.lower():
        if ch not in vowels:
            result.append("." + ch)

    print("".join(result))

# CLAUSE: finish_program
def main():
    _inner_main()

main()
