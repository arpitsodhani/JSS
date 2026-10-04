import sys

def can_win(hc, dc, hm, dm):
    hero_turns = (hm + dc - 1) // dc
    monster_turns = (hc + dm - 1) // dm
    return hero_turns <= monster_turns

def main():
    data = list(map(int, sys.stdin.read().split()))
    t = data[0]
    idx = 1
    out = []
    
    for _ in range(t):
        hc = data[idx]
        dc = data[idx + 1]
        idx += 2
        
        hm = data[idx]
        dm = data[idx + 1]
        idx += 2
        
        k = data[idx]
        w = data[idx + 1]
        a = data[idx + 2]
        idx += 3
        
        ok = False
        for weapon_upgrades in range(k + 1):
            armor_upgrades = k - weapon_upgrades
            new_hc = hc + armor_upgrades * a
            new_dc = dc + weapon_upgrades * w
            
            if can_win(new_hc, new_dc, hm, dm):
                ok = True
                break
        
        out.append("YES" if ok else "NO")
    
    print('\n'.join(out))

if __name__ == "__main__":
    main()
