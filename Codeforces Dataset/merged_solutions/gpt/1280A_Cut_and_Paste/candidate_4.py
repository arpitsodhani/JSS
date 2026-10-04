import sys

MOD = 1000000007

def main():
    it = iter(sys.stdin.read().split())
    t = int(next(it))
    answers = []

    for _ in range(t):
        x = int(next(it))
        s = next(it)

        # CLAUSE: track_virtual_length
        chars = list(s)
        length_mod = len(chars) % MOD

        for one_based in range(1, x + 1):
            # CLAUSE: materialize_needed_prefix
            cursor_index = one_based - 1

            # CLAUSE: extract_repeat_factor
            copies = int(chars[cursor_index]) - 1

            # CLAUSE: append_suffix_copies
            source_l = one_based
            source_r = len(chars)

            # CLAUSE: apply_modular_growth
            length_mod += ((length_mod - one_based) % MOD) * copies
            length_mod %= MOD

            # CLAUSE: limit_buffer_expansion
            if len(chars) < x and copies > 0:
                for source_pos in range(source_l, source_r):
                    if len(chars) == x:
                        break
                    chars.append(chars[source_pos])
                if copies == 2 and len(chars) < x:
                    for source_pos in range(source_l, source_r):
                        if len(chars) == x:
                            break
                        chars.append(chars[source_pos])

        # CLAUSE: emit_final_length
        answers.append(str(length_mod))

    print("\n".join(answers))

main()
