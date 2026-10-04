import sys

MOD = 1_000_000_007

raw = sys.stdin.buffer.read().split()
tc = int(raw[0])
ptr = 1
printed = []

for _ in range(tc):
    x = int(raw[ptr])
    initial = raw[ptr + 1].decode()
    ptr += 2

    # CLAUSE: track_virtual_length
    prefix = initial
    effective = len(prefix)

    for cur in range(x):
        # CLAUSE: materialize_needed_prefix
        digit = prefix[cur]

        # CLAUSE: extract_repeat_factor
        repeat_count = int(digit) - 1

        # CLAUSE: append_suffix_copies
        segment = prefix[cur + 1:]

        # CLAUSE: apply_modular_growth
        effective = (effective + (effective - cur - 1) * repeat_count) % MOD

        # CLAUSE: limit_buffer_expansion
        if len(prefix) < x:
            remaining = x - len(prefix)
            expanded = segment * repeat_count
            prefix += expanded[:remaining]

    # CLAUSE: emit_final_length
    printed.append(str(effective))

sys.stdout.write("\n".join(printed))
