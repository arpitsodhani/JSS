# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def _run_case_program():
    s = input().strip()
    vowels = set("aoyeui")
    result = []

    for ch in s.lower():
        if ch not in vowels:
            result.append("." + ch)

    print("".join(result))

# CLAUSE: finish_program
if __name__ == "__main__":
    _run_case_program()
