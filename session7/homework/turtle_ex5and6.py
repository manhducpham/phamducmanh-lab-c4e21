from turtle import *

# 5
def draw_star(x, y, length):
    penup()
    goto(x, y)
    pendown()
    left(72)
    for i in range (5):
        forward(length)
        right(144)

# draw_star(-100, -100, 100)
# mainloop()

#6
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
