import math
import sys

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

def min_dist_point_to_segment(px, py, x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    if dx == 0 and dy == 0:
        return distance(px, py, x1, y1)
    
    t = ((px - x1) * dx + (py - y1) * dy) / (dx*dx + dy*dy)
    t = max(0, min(1, t))
    
    closest_x = x1 + t * dx
    closest_y = y1 + t * dy
    return distance(px, py, closest_x, closest_y)

def shortest_path_avoiding_circle(x1, y1, x2, y2, r):
    if distance(x1, y1, x2, y2) < 1e-9:
        return 0
    
    # Check if straight line works
    min_dist = min_dist_point_to_segment(0, 0, x1, y1, x2, y2)
    if min_dist >= r - 1e-9:
        return distance(x1, y1, x2, y2)
    
    d1 = distance(0, 0, x1, y1)
    d2 = distance(0, 0, x2, y2)
    
    if d1 < r - 1e-9 or d2 < r - 1e-9:
        return float('inf')
    
    theta1 = math.atan2(y1, x1)
    theta2 = math.atan2(y2, x2)
    
    # Compute tangent point angles using arccos
    beta1 = math.acos(min(1.0, r / d1))
    beta2 = math.acos(min(1.0, r / d2))
    
    tang_angles1 = [theta1 - beta1, theta1 + beta1]
    tang_angles2 = [theta2 - beta2, theta2 + beta2]
    
    min_path = float('inf')
    
    for ta1 in tang_angles1:
        for ta2 in tang_angles2:
            tx1, ty1 = r * math.cos(ta1), r * math.sin(ta1)
            tx2, ty2 = r * math.cos(ta2), r * math.sin(ta2)
            
            d_to_t1 = distance(x1, y1, tx1, ty1)
            d_from_t2 = distance(tx2, ty2, x2, y2)
            
            arc_angle = ta2 - ta1
            while arc_angle > math.pi:
                arc_angle -= 2 * math.pi
            while arc_angle < -math.pi:
                arc_angle += 2 * math.pi
            arc_length = r * abs(arc_angle)
            
            total = d_to_t1 + arc_length + d_from_t2
            min_path = min(min_path, total)
    
    return min_path

def get_persephone_pos(x_p, y_p, R, v_p, t):
    theta_0 = math.atan2(y_p, x_p)
    omega = v_p / R
    theta_t = theta_0 + omega * t
    return R * math.cos(theta_t), R * math.sin(theta_t)

def can_reach(x, y, v, px, py, r, t):
    path_length = shortest_path_avoiding_circle(x, y, px, py, r)
    return path_length <= v * t + 1e-9

def solve():
    data = sys.stdin.read().strip().split()
    x_p = float(data[0])
    y_p = float(data[1])
    v_p = float(data[2])
    x = float(data[3])
    y = float(data[4])
    v = float(data[5])
    r = float(data[6])
    
    R = math.sqrt(x_p**2 + y_p**2)
    
    if distance(x, y, x_p, y_p) < 1e-9:
        print("0.000000000")
        return
    
    left, right = 0.0, 1e6
    
    for _ in range(150):
        mid = (left + right) / 2
        px, py = get_persephone_pos(x_p, y_p, R, v_p, mid)
        
        if can_reach(x, y, v, px, py, r, mid):
            right = mid
        else:
            left = mid
    
    print(f"{right:.10f}")

solve()
