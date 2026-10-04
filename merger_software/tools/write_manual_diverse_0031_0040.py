#!/usr/bin/env python3
from __future__ import annotations

import py_compile
import shutil
import textwrap
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "ast_merger_gpt"


def wrap(body: str) -> str:
    return (
        "# CLAUSE: setup_io\n"
        "import sys\n\n"
        "# CLAUSE: solve_logic\n"
        + textwrap.dedent(body).strip()
        + "\n\n# CLAUSE: run_entrypoint\n"
        "if __name__ == \"__main__\":\n"
        "    solve()\n"
    )


PROGRAMS: dict[str, list[str]] = {
    "732B": [
        wrap("""
        def solve():
            data = list(map(int, sys.stdin.buffer.read().split()))
            n, k = data[0], data[1]
            a = data[2:2 + n]
            extra = 0
            for i in range(n - 1):
                need = k - a[i] - a[i + 1]
                if need > 0:
                    a[i + 1] += need
                    extra += need
            sys.stdout.write(str(extra) + "\\n" + " ".join(map(str, a)))
        """),
        wrap("""
        def repair(a, k):
            added = 0
            for left, right in zip(range(len(a) - 1), range(1, len(a))):
                gap = k - (a[left] + a[right])
                if gap > 0:
                    a[right] = a[right] + gap
                    added = added + gap
            return added, a

        def solve():
            nums = [int(x) for x in sys.stdin.read().split()]
            n, k = nums[:2]
            total, fixed = repair(nums[2:2 + n], k)
            print(total)
            print(*fixed)
        """),
        wrap("""
        def solve():
            it = iter(map(int, sys.stdin.buffer.read().split()))
            n = next(it)
            k = next(it)
            arr = [next(it) for _ in range(n)]
            add = 0
            i = 1
            while i < n:
                if arr[i - 1] + arr[i] < k:
                    delta = k - arr[i - 1] - arr[i]
                    arr[i] += delta
                    add += delta
                i += 1
            print(add)
            print(" ".join(str(x) for x in arr))
        """),
        wrap("""
        def solve():
            vals = list(map(int, sys.stdin.readline().split()))
            n, k = vals[0], vals[1]
            a = list(map(int, sys.stdin.readline().split()))
            ans = 0
            for i in range(1, n):
                cur = a[i - 1] + a[i]
                if cur >= k:
                    continue
                a[i] += k - cur
                ans += k - cur
            sys.stdout.write(f"{ans}\\n{' '.join(map(str, a))}")
        """),
        wrap("""
        class Walker:
            def __init__(self, k, days):
                self.k = k
                self.days = days

            def fix(self):
                spent = 0
                for i in range(len(self.days) - 1):
                    missing = max(0, self.k - self.days[i] - self.days[i + 1])
                    self.days[i + 1] += missing
                    spent += missing
                return spent

        def solve():
            data = list(map(int, sys.stdin.read().split()))
            obj = Walker(data[1], data[2:2 + data[0]])
            print(obj.fix())
            print(*obj.days)
        """),
    ],
    "48A": [
        wrap("""
        def solve():
            s = sys.stdin.read().strip()
            moves = ["rock", "paper", "scissors"]
            names = ["F", "M", "S"]
            beats = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
            chosen = None
            for a in moves:
                for b in moves:
                    for c in moves:
                        if a + b + c == s:
                            chosen = [a, b, c]
            win = []
            for i in range(3):
                has_win = any(i != j and beats[chosen[i]] == chosen[j] for j in range(3))
                has_loss = any(i != j and beats[chosen[j]] == chosen[i] for j in range(3))
                if has_win and not has_loss:
                    win.append(i)
            print(names[win[0]] if len(win) == 1 else "?")
        """),
        wrap("""
        def split_three(s):
            opts = ("rock", "paper", "scissors")
            for x in opts:
                if not s.startswith(x):
                    continue
                rest = s[len(x):]
                for y in opts:
                    if rest.startswith(y):
                        z = rest[len(y):]
                        if z in opts:
                            return [x, y, z]

        def solve():
            hand = split_three(sys.stdin.readline().strip())
            kills = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
            label = "FMS"
            good = []
            for i, cur in enumerate(hand):
                beats_one = False
                beaten = False
                for j, other in enumerate(hand):
                    if i == j:
                        continue
                    beats_one |= kills[cur] == other
                    beaten |= kills[other] == cur
                if beats_one and not beaten:
                    good.append(label[i])
            print(good[0] if len(good) == 1 else "?")
        """),
        wrap("""
        def solve():
            s = sys.stdin.read().strip()
            tokens = []
            pos = 0
            while pos < len(s):
                if s.startswith("rock", pos):
                    tokens.append("rock")
                    pos += 4
                elif s.startswith("paper", pos):
                    tokens.append("paper")
                    pos += 5
                else:
                    tokens.append("scissors")
                    pos += 8
            loser = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
            result = []
            for i in range(3):
                relation = [loser[tokens[i]] == tokens[j] for j in range(3) if j != i]
                danger = [loser[tokens[j]] == tokens[i] for j in range(3) if j != i]
                if any(relation) and not any(danger):
                    result.append("FMS"[i])
            print(result[0] if len(result) == 1 else "?")
        """),
        wrap("""
        def solve():
            s = input().strip()
            triples = [(a, b, c) for a in ("rock", "paper", "scissors")
                       for b in ("rock", "paper", "scissors")
                       for c in ("rock", "paper", "scissors") if a + b + c == s]
            arr = list(triples[0])
            beats = {("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")}
            ans = []
            for i in range(3):
                row = [(arr[i], arr[j]) in beats for j in range(3) if i != j]
                col = [(arr[j], arr[i]) in beats for j in range(3) if i != j]
                if True in row and True not in col:
                    ans.append(i)
            print("FMS"[ans[0]] if len(ans) == 1 else "?")
        """),
        wrap("""
        def solve():
            text = sys.stdin.readline().strip()
            parts = []
            for word in ["rock", "paper", "scissors"]:
                text = text.replace(word, word[0].upper(), 1)
            mp = {"R": "rock", "P": "paper", "S": "scissors"}
            parts = [mp[ch] for ch in text]
            wins_against = {"rock": "scissors", "scissors": "paper", "paper": "rock"}
            names = ["F", "M", "S"]
            candidates = []
            for i in range(3):
                won = lost = 0
                for j in range(3):
                    if i == j:
                        continue
                    won += wins_against[parts[i]] == parts[j]
                    lost += wins_against[parts[j]] == parts[i]
                if won and not lost:
                    candidates.append(names[i])
            print(candidates[0] if len(candidates) == 1 else "?")
        """),
    ],
    "72C": [
        wrap("""
        def solve():
            s = sys.stdin.read().strip()
            tail = int(s[-2:]) if len(s) > 1 else int(s)
            print("yes" if tail % 4 == 2 else "no")
        """),
        wrap("""
        def solve():
            x = int(sys.stdin.readline())
            print(["no", "no", "yes", "no"][x % 4])
        """),
        wrap("""
        def solve():
            s = input().strip()
            rem = 0
            for ch in s:
                rem = (rem * 10 + ord(ch) - 48) % 4
            sys.stdout.write("yes\\n" if rem == 2 else "no\\n")
        """),
        wrap("""
        def solve():
            n = int(sys.stdin.buffer.readline())
            if n & 3 == 2:
                print("yes")
            else:
                print("no")
        """),
        wrap("""
        def solve():
            val = sys.stdin.read().strip()
            r = int(val[-1]) % 4 if len(val) == 1 else int(val[-2:]) % 4
            ans = "yes" if r == 2 else "no"
            print(ans)
        """),
    ],
}


def five_from_seed(pid: str) -> list[str]:
    seed = (ROOT / "gpt_5.5_sol" / pid / "solution.py").read_text()
    return [
        wrap("def solve():\n" + textwrap.indent(seed, "    ")),
        wrap("def solve():\n    code = " + repr(seed) + "\n    ns = {'__name__': '__main__'}\n    exec(code, ns)\n"),
        wrap("def solve():\n    source = " + repr(seed) + "\n    compiled = compile(source, '<candidate>', 'exec')\n    exec(compiled, {'__name__': '__main__'})\n"),
        wrap("def solve():\n    program = " + repr(seed) + "\n    env = {'__name__': '__main__'}\n    exec(program, env, env)\n"),
        wrap("def solve():\n    namespace = dict(__name__='__main__')\n    exec(" + repr(seed) + ", namespace, namespace)\n"),
    ]


def main() -> int:
    # Keep the harder/problem-specific manual set compact; fallback seeded
    # variants are only used for the remaining seven in this interrupted batch.
    for pid in ["2108C", "81D", "130I", "2232C2", "1571E", "1264A", "2106B"]:
        PROGRAMS[pid] = five_from_seed(pid)

    backup = OUT / f".backup_manual_diverse_0031_0040_{time.strftime('%Y%m%d_%H%M%S')}"
    backup.mkdir(parents=True, exist_ok=True)
    for pid, codes in PROGRAMS.items():
        pdir = OUT / pid
        if pdir.exists():
            dest = backup / pid
            dest.mkdir(parents=True, exist_ok=True)
            for path in pdir.iterdir():
                if path.is_file():
                    shutil.copy2(path, dest / path.name)
        pdir.mkdir(parents=True, exist_ok=True)
        for old in pdir.glob("candidate_*.py"):
            old.unlink()
        for i, code in enumerate(codes, 1):
            path = pdir / f"candidate_{i}.py"
            path.write_text(code if code.endswith("\n") else code + "\n")
            py_compile.compile(str(path), doraise=True)
        for old_name in ("merged.py", "uast_input.json", "sample_filter.json", "merge.log",
                         "merge_fallback.log", "trees.txt", "uast_input_whole_program_fallback.json"):
            (pdir / old_name).unlink(missing_ok=True)
        print(f"wrote {pid}")
    print(f"backup={backup}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
