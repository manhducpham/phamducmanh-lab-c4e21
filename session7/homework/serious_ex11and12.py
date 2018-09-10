# 11
def is_inside(point, rectangle):
    [x1, y1] = point
    [x2, y2, w, h] =  rectangle
    test_x = x2 <= x1 <= (x2 + w) 
    test_y = y2 <= y1 <= (y2 +h)
    if test_x and test_y:
        return True
    else:
        return False
# 12. Test case
test_1 = is_inside([200, 120], [140, 60, 100, 200])
test_2 = is_inside([100, 120], [140, 60, 100, 200])
# print(test_1, test_2)
if test_1 and not test_2:
    print("Your function is correct")
else:
    print("Ooops, bugs detected")