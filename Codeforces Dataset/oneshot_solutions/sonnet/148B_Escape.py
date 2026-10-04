import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    vp, vd, t, f, c = data
    
    if vd <= vp:
        print(0)
        return
    
    princess = vp * t
    bijous = 0
    
    while princess < c:
        catch_time = princess / (vd - vp)
        catch_pos = vd * catch_time
        
        if catch_pos >= c:
            break
        
        bijous += 1
        
        return_time = catch_pos / vd
        princess = catch_pos + vp * (return_time + f)
    
    print(bijous)

if __name__ == "__main__":
    main()
