from random import randint, choice
from calc import calculate

x = randint(0, 9)
y = randint(0, 9)
op = choice(['+', '-', '*', '/'])
# print(op)
error = randint(-1, 1)

r = calculate(x, y, op) + error
print(x, op, y, '=', r)

user_answer = input("(Y/N)? ").upper()
if calculate(x, y, op) == r:
    if user_answer == "Y":
        print('Yay')
    elif user_answer =="N":
        print('Nah')
else:
    if user_answer == "Y":
        print('Nah')
    elif user_answer == "N":
        print("Yay")