
def is_inside(point, rectangle):
    [x1, y1] = point
    [x2, y2, w, h] =  rectangle
    test_x = x2 <= x1 <= (x2 + w) 
    test_y = y2 <= y1 <= (y2 +h)
    if test_x and test_y:
        return True
    else:
        return False