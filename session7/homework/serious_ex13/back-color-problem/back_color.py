from random import *
from test_click import is_inside
shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]
text_list = []
color_list = []
for item in shapes:
    item_text = item['text'].upper()
    item_color = item['color']
    text_list.append(item_text)
    color_list.append(item_color)
# print(text_list, color_list)

def get_shapes():
    return shapes


def generate_quiz():
    text_rand = choice(text_list)
    color_rand = choice(color_list)
    return [
                text_rand,
                color_rand,
                randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    point = [x, y]
    if quiz_type == 0:
        text_pos = text_list.index(text)
        rectangle = shapes[text_pos]['rect']
    elif quiz_type == 1:
        color_pos = color_list.index(color)
        rectangle = shapes[color_pos]['rect']
    test = is_inside(point, rectangle)
    return test