# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
class ProgramRunner:
    @staticmethod
    def run():
        import sys

        data = list(map(int, sys.stdin.read().split()))
        t = data[0]
        idx = 1
        ans = []

        for _ in range(t):
            hC, dC, hM, dM = data[idx:idx + 4]
            idx += 4
            k, w, a = data[idx:idx + 3]
            idx += 3

            ok = False
            for weapon in range(k + 1):
                armor = k - weapon
                hp = hC + armor * a
                dmg = dC + weapon * w

                hero_turns = (hM + dmg - 1) // dmg
                monster_turns = (hp + dM - 1) // dM

                if hero_turns <= monster_turns:
                    ok = True
                    break

            ans.append("YES" if ok else "NO")

        print("\n".join(ans))

# CLAUSE: finish_program
if __name__ == "__main__":
    ProgramRunner.run()
