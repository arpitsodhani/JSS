# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
def choose_new_pin(pin, blocked):
    chars = list(pin)
    for position in range(3, -1, -1):
        saved = chars[position]
        for value in range(10):
            digit = str(value)
            if digit == saved:
                continue
            chars[position] = digit
            made = "".join(chars)
            if made not in blocked:
                return made
        chars[position] = saved
    return pin

def main():
    values = iter(sys.stdin.read().split())
    tests = int(next(values))
    rows = []

    for _ in range(tests):
        n = int(next(values))
        pins = [next(values) for _ in range(n)]
        first_places = {}
        duplicate_indices = []

        for idx, pin in enumerate(pins):
            if pin in first_places:
                duplicate_indices.append(idx)
            else:
                first_places[pin] = idx

        taken = set(pins)
        for idx in duplicate_indices:
            new_pin = choose_new_pin(pins[idx], taken)
            pins[idx] = new_pin
            taken.add(new_pin)

        rows.append(str(len(duplicate_indices)))
        rows.extend(pins)

    print("\n".join(rows))

# CLAUSE: finish_program
main()
