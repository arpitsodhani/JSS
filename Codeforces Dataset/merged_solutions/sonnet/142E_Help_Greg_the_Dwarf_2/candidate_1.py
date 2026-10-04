# CLAUSE: setup_environment
import sys

# CLAUSE: solve_logic
import math
import sys

def solve():
    data = sys.stdin.read().split()
    r = float(data[0])
    h = float(data[1])
    x1, y1, z1 = float(data[2]), float(data[3]), float(data[4])
    x2, y2, z2 = float(data[5]), float(data[6]), float(data[7])
    
    rho1 = math.sqrt(x1**2 + y1**2)
    phi1 = math.atan2(y1, x1)
    
    rho2 = math.sqrt(x2**2 + y2**2)
    phi2 = math.atan2(y2, x2)
    
    # Slant height of cone
    L = math.sqrt(r**2 + h**2)
    # Sector angle when unrolled
    alpha = 2 * math.pi * r / L
    
    def dist_unrolled(s1, theta1, s2, theta2):
        # Distance in unrolled cone, considering wrapping
        min_d = float('inf')
        for k in range(-10, 11):
            d = math.sqrt(s1**2 + s2**2 - 2*s1*s2*math.cos(theta2 - theta1 + k*alpha))
            min_d = min(min_d, d)
        return min_d
    
    # Map to unrolled coordinates
    s1 = (h - z1) * L / h
    theta1 = phi1 * alpha / (2 * math.pi)
    
    s2 = (h - z2) * L / h
    theta2 = phi2 * alpha / (2 * math.pi)
    
    min_dist = float('inf')
    
    # Direct path on cone surface
    min_dist = min(min_dist, dist_unrolled(s1, theta1, s2, theta2))
    
    # Paths via base (reflection through z=0 plane)
    s2_refl = (h + z2) * L / h
    min_dist = min(min_dist, dist_unrolled(s1, theta1, s2_refl, theta2))
    
    s1_refl = (h + z1) * L / h
    min_dist = min(min_dist, dist_unrolled(s1_refl, theta1, s2, theta2))
    
    # If point is in base disk interior, try path via base circle
    eps = 1e-9
    if z1 < eps and rho1 < r - eps:
        for i in range(360):
            phi_q = -math.pi + 2 * math.pi * i / 360
            xq, yq = r * math.cos(phi_q), r * math.sin(phi_q)
            d1 = math.sqrt((x1-xq)**2 + (y1-yq)**2)
            
            theta_q = phi_q * alpha / (2 * math.pi)
            d2 = dist_unrolled(L, theta_q, s2, theta2)
            
            min_dist = min(min_dist, d1 + d2)
    
    if z2 < eps and rho2 < r - eps:
        for i in range(360):
            phi_q = -math.pi + 2 * math.pi * i / 360
            xq, yq = r * math.cos(phi_q), r * math.sin(phi_q)
            d2 = math.sqrt((x2-xq)**2 + (y2-yq)**2)
            
            theta_q = phi_q * alpha / (2 * math.pi)
            d1 = dist_unrolled(s1, theta1, L, theta_q)
            
            min_dist = min(min_dist, d1 + d2)
    
    # If both on base disk, Euclidean distance
    if z1 < eps and z2 < eps:
        min_dist = min(min_dist, math.sqrt((x1-x2)**2 + (y1-y2)**2))
    
    print(f"{min_dist:.9f}")

solve()

# CLAUSE: finish_program
RESULT_SENTINEL = None
