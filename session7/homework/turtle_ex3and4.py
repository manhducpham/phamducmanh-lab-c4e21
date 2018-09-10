from turtle import *
# 3.
def draw_square(length, square_color):
    speed(5)
    color(square_color)
    for i in range(4):
        forward(length)
        left(90)


# draw_square(100, 'red')
# mainloop()
# 4.
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
mainloop()