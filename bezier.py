from vec import Vec

def quadratic_curve(vecs, t):
    p0 = Vec((1-t) ** 2 * vecs[0].x, (1-t) ** 2 * vecs[0].y)
    p1 = Vec(2 * (1-t) * t * vecs[1].x, 2 * (1-t) * t * vecs[1].y)
    p2 = Vec(t ** 2 * vecs[2].x, t ** 2 * vecs[2].y)

    return p0 + p1 + p2

def quadratic_curve_length(vecs):
    t = 0
    step = 0.05
    dist = 0
    
    pos = quadratic_curve(vecs, 0)

    while t < 1:
       t += step 

       new_pos = quadratic_curve(vecs, t)
       dist += (new_pos - pos).magnitude()

    return dist
